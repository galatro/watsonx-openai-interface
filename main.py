from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/") 
def read_root(): 
    return {"message": "Watsonx Openai interface"} 

@app.get("/health") 
def health_check(): 
    return {"status": "healthy"}


if __name__ == "__main__": 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

