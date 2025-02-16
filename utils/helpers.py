from tabulate import tabulate
import time
import uuid


def format_debug_output(request_data):
    """
    Generates a formatted table displaying API parameters, their values, and explanations.
    Highlights whether the values are provided by the API or defaulted.
    """
    headers = ["Provided by API", "Parameter", "API Value", "Default Value", "Explanation"]
    table = []

    # Define parameter mappings with improved explanations
    parameters = [
        ("Model ID", request_data.model, "ibm/granite-20b-multilingual",
         "Unique identifier of the model to use for text generation."),

        ("Max Tokens", request_data.max_tokens, 2000,
         "The maximum number of tokens to generate. Includes both prompt and output tokens."),

        ("Temperature", request_data.temperature, 0.2,
         "Controls randomness. Lower values make output more deterministic; higher values increase variation."),

        ("Presence Penalty", request_data.presence_penalty, 1,
         "Discourages repetition of existing words. Higher values encourage diversity in topics."),

        ("Top-p", request_data.top_p, 1,
         "Nucleus sampling: Limits token selection to a probability mass of p (e.g., 0.1 considers only the top 10%)."),

        ("Best of", request_data.best_of, 1,
         "Generates multiple completions and selects the one with the highest likelihood."),

        ("Echo", request_data.echo, False,
         "If enabled, returns both the input prompt and generated completion for debugging."),

        ("Number of Completions", request_data.n, 1,
         "Specifies how many completions to generate per request. High values consume more tokens."),

        ("Seed", request_data.seed, None,
         "Ensures deterministic results. Using the same seed with identical parameters will yield the same output."),

        ("Stop Sequences", request_data.stop, None,
         "Defines specific sequences that will terminate text generation when encountered."),

        ("Logit Bias", request_data.logit_bias, None,
         "Adjusts token probabilities. Accepts a dictionary mapping token IDs to bias values (-100 to 100)."),

        ("Log Probabilities", request_data.logprobs, None,
         "Returns log probabilities for the most likely tokens, useful for analyzing model behavior."),

        ("Stream", request_data.stream, False,
         "Enables real-time token streaming, useful for responsive applications."),

        ("Suffix", request_data.suffix, None,
         "Appends a specific string after the generated text, useful for structured output formatting.")
    ]

    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

    for param, api_value, default_value, explanation in parameters:
        if api_value is not None:
            color = MAGENTA  # Highlight API-provided values in yellow
            provided_by_api = f"{MAGENTA}✔{RESET}"
        else:
            color = CYAN  # Highlight default values in green
            provided_by_api = ""

        table.append([
            provided_by_api,
            f"{color}{param}{RESET}",
            f"{color}{api_value}{RESET}" if api_value is not None else f"{color}{default_value}{RESET}",
            f"{color}{default_value}{RESET}",
            f"{color}{explanation}{RESET}"
        ])

    return tabulate(table, headers, tablefmt="pretty", colalign=("center", "left", "center", "center", "left"))


def convert_watsonx_to_openai_format(watsonx_data):
    """
    Converts Watsonx model metadata to an OpenAI-compatible JSON format.
    """
    openai_models = []
    for model in watsonx_data:
        openai_model = {
            "id": model['model_id'],
            "object": "model",
            "created": int(time.time()),
            "owned_by": f"{model['provider']} / {model['source']}",
            "description": f"{model['short_description']} Supports: {', '.join(model.get('task_ids', []))}.",
            "max_tokens": model['model_limits']['max_output_tokens'],
            "token_limits": {
                "max_sequence_length": model['model_limits']['max_sequence_length'],
                "max_output_tokens": model['model_limits']['max_output_tokens']
            }
        }
        openai_models.append(openai_model)
    return {"data": openai_models}


def format_openai_response(results):
    """
    Formats Watsonx completion results into an OpenAI-style response structure.
    """
    return {
        "id": f"cmpl-{str(uuid.uuid4())[:12]}",
        "object": "text_completion",
        "created": int(time.time()),
        "model": results['model_id'],
        "system_fingerprint": f"fp_{str(uuid.uuid4())[:12]}",
        "choices": [
            {
                "text": results['results'][0].get("generated_text"),
                "index": 0,
                "logprobs": None,
                "finish_reason": results['results'][0].get("stop_reason", "length")
            }
        ],
        "usage": {
            "prompt_tokens": results['results'][0]["input_token_count"],
            "completion_tokens": results['results'][0]["generated_token_count"],
            "total_tokens": results['results'][0]["input_token_count"] + results['results'][0]["generated_token_count"]
        }
    }
