from pydantic_settings import BaseSettings
from typing import ClassVar

class Settings(BaseSettings):
    WATSONX_URL: str
    WATSONX_PROJECT_ID: str
    IBM_API_KEY: str
    MODEL_DEFAULTS: ClassVar[dict] = {
        "default_model": "ibm/granite-20b-multilingual",
        "max_tokens": 2000,
        "temperature": 0.2
    }
    
    class Config:
        env_file = ".env"

settings = Settings()
