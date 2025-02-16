from fastapi import APIRouter, HTTPException
from api.models import CompletionRequest, EmbeddingRequest
from controllers import models_controller, completion_controller, embedding_controller
from utils.errors import ModelNotFoundError, CompletionError, EmbeddingError

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/models")
async def fetch_models_route():
    try:
        return await models_controller.fetch_models()
    except ModelNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models/{model_id}")
async def fetch_model_by_id_route(model_id: str):
    try:
        return await models_controller.fetch_model_by_id(model_id)
    except ModelNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/completions")
async def completions_route(request: CompletionRequest):
    try:
        return await completion_controller.create_completion(request)
    except CompletionError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
