from fastapi import APIRouter 
from app.models import CompletionRequest 
from typing import List 

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/models")
async def fetch_models():
    pass

@router.get("/models/{model_id}")
async def fetch_model_by_id(model_id: str):
    pass

@router.post("/completions")
async def watsonx_completions(request: CompletionRequest):
    pass
