from fastapi import HTTPException
import logging

from utils.helpers import convert_watsonx_to_openai_format
from watsonx.client import watsonx_client

logger = logging.getLogger(__name__)

async def fetch_models():
    try:
        models = watsonx_client.client.foundation_models.get_model_specs()
        logger.debug(f"Available models: {models}")
        return convert_watsonx_to_openai_format(models['resources'])
    except Exception as err:
        logger.error(f"Error fetching models: {err}")
        raise HTTPException(status_code=500, detail=f"Error fetching models: {err}")

async def fetch_model_by_id(model_id: str):
    try:
        model = watsonx_client.client.foundation_models.get_model_specs(id=model_id)
        if model:
            return convert_watsonx_to_openai_format([model])
        raise HTTPException(status_code=404, detail=f"Model with ID {model_id} not found.")
    except Exception as err:
        logger.error(f"Error fetching model by ID: {err}")
        raise HTTPException(status_code=500, detail=f"Error fetching model by ID: {err}")