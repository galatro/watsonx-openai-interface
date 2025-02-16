from ibm_watsonx_ai import APIClient, Credentials
import os
import logging

from config.settings import settings
from utils.errors import WatsonXConfigError

class WatsonxClient:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WatsonxClient, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.logger = logging.getLogger(__name__)
        try:
            self.credentials = Credentials(
                url=settings.WATSONX_URL,
                api_key=settings.IBM_API_KEY
            )
            self.client = APIClient(self.credentials)
            self.project_id = settings.WATSONX_PROJECT_ID
        except Exception as e:
            raise WatsonXConfigError(f"Failed to initialize WatsonX client: {str(e)}")
        
watsonx_client=WatsonxClient()