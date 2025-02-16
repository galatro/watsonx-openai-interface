from fastapi import FastAPI
from api.v1.routes import router
from utils.logging import setup_logging

import uvicorn

# Initialize logging
setup_logging()

# Initialize FastAPI application
app = FastAPI()

@app.get("/") 
def read_root(): 
    return {"message": "Watsonx Openai interface"} 

@app.get("/health") 
def health_check(): 
    return {"status": "healthy"}

# Include API routes
app.include_router(router)

if __name__ == "__main__": 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

