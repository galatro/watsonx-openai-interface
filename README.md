# OpenAI Interface with Watsonx

This project implements an OpenAI-compatible interface using IBM Watsonx.ai . It supports legacy OpenAI AI endpoints for compatibility, providing access to model completions and model retrieval functionalities.

## Features

- **Completions API (Legacy)**: Generates text completions based on a given prompt.
- **Model Retrieval APIs**: Fetches a list of available models or details about a single model.
- **Uses OpenAI-Compatible API**: Enables existing OpenAI clients to interact with Watsonx models.

## API Endpoints

### 1. Completions (Legacy)

**Endpoint:**

```
POST https://api.openai.com/v1/completions
```

**Description:** Given a prompt, the model generates one or more completions along with probabilities of alternative tokens. Most developers should use the Chat Completions API for newer models, but this legacy endpoint is supported for compatibility.

**Request Body Parameters:**

- `model` (string, required): ID of the model to use.
- `prompt` (string or array, required): The input prompt for completion.
- `max_tokens` (integer, optional, default: 16): Maximum number of tokens to generate.
- `temperature` (number, optional, default: 1): Controls randomness (0-2 range).
- `top_p` (number, optional, default: 1): Alternative to temperature, controls nucleus sampling.
- `n` (integer, optional, default: 1): Number of completions to generate.
- `stream` (boolean, optional, default: false): Enables streaming responses.
- Other OpenAI completion parameters are also supported.

**Response:** Returns a completion object containing the generated text.

---

### 2. List Models

**Endpoint:**

```
GET https://api.openai.com/v1/models
```

**Description:** Returns a list of available models, including basic metadata.

**Response (Legacy API Example):**

```json
{
  "id": "mistralai/mixtral-8x7b-instruct-v01",
  "object": "model",
  "created": 1739635440,
  "owned_by": "Mistral AI / Hugging Face",
  "description": "The Mixtral-8x7B Large Language Model (LLM) is a pretrained generative Sparse Mixture of Experts. Supports: question_answering, summarization, retrieval_augmented_generation, classification, generation, code, extraction, translation.",
  "max_tokens": 16384,
  "token_limits": {
    "max_sequence_length": 32768,
    "max_output_tokens": 16384
  }
}
```

**New API Response Format:**
The output provided is richer respect the new OpenAI API Response format and contains more information.

```json

{
    "id": "model-id-0",
    "object": "model",
    "created": 1686935002,
    "owned_by": "organization-owner"
}
```

## Running the Application

### Prerequisites

Ensure you have the necessary environment variables set up in an `.env` file:

```bash
IBM_API_KEY=your_ibm_api_key
WATSONX_PROJECT_ID=your_watsonx_project_id
WATSONX_REGION=your_watsonx_region
```

### Using Docker/Podman

Run the following command to start the container:

```bash
docker build -t watsonxai-endpoint .

source ./.env
podman run -d -p 8080:8000 --name watsonxai-endpoint \
-e IBM_API_KEY=${IBM_API_KEY} \
-e WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID} \
-e WATSONX_REGION=${WATSONX_REGION}
```


## Conclusion

This project provides an OpenAI-compatible API using IBM Watsonx, maintaining support for legacy endpoints while offering robust AI capabilities. It ensures a seamless transition for existing OpenAI API users while leveraging Watsonx’s advanced models.

