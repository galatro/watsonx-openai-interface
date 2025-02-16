class WatsonXConfigError(Exception):
    """Raised when WatsonX configuration is invalid"""
    pass

class ModelNotFoundError(Exception):
    """Raised when requested model is not found"""
    pass

class CompletionError(Exception):
    """Raised when text completion fails"""
    pass

