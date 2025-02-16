from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
import json
import logging

from utils.helpers import format_debug_output, format_openai_response
from api.models import CompletionRequest
from watsonx.client import watsonx_client

logger = logging.getLogger(__name__)


async def watsonx_completions(request: CompletionRequest):
    logger.info("Received a Watsonx completion request.")
    generate_params = {
        GenParams.MAX_NEW_TOKENS: request.max_tokens,
        GenParams.TEMPERATURE: request.temperature,
        GenParams.REPETITION_PENALTY: request.presence_penalty,
        GenParams.TOP_P: request.top_p,
        GenParams.TOP_K: 50,
        GenParams.DECODING_METHOD: 'sample',
    }
    if request.stop:
        if isinstance(request.stop, str):
            generate_params[GenParams.STOP_SEQUENCES] = [request.stop]
        else:
            generate_params[GenParams.STOP_SEQUENCES] = request.stop

    if request.seed:
        generate_params[GenParams.RANDOM_SEED] = request.seed
    
    logger.debug("Parameter source debug:")
    logger.debug("\n" + format_debug_output(request_data=request))
    
    model_inference = ModelInference(
        model_id=request.model,
        params=generate_params,
        api_client=watsonx_client.client,
        project_id=watsonx_client.project_id
    )
    
    prompt = request.prompt if isinstance(request.prompt, str) else " ".join(request.prompt)
    wx_response = model_inference.generate(prompt=prompt)
    logger.debug(f"Received response from Watsonx.ai: {json.dumps(wx_response, indent=4)}")
    openai_response = format_openai_response(wx_response)
    
    logger.debug(f"Returning OpenAI-compatible response: {json.dumps(openai_response, indent=4)}")
    return openai_response
