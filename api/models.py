from typing import Optional, List, Dict, Union, Literal
from pydantic import BaseModel

class CompletionRequest(BaseModel):
    model: str = "ibm/granite-20b-multilingual"
    prompt: Union[str, List[str]]
    max_tokens: Optional[int] = 2000
    temperature: Optional[float] = 0.2
    best_of: Optional[int] = 1
    n: Optional[int] = 1
    presence_penalty: Optional[float] = 1.0
    echo: Optional[bool] = False
    logit_bias: Optional[Dict[str, float]] = None
    logprobs: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    suffix: Optional[str] = None
    stream: Optional[bool] = False
    seed: Optional[int] = None
    top_p: Optional[float] = 1.0

