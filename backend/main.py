# ../backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
# from transformers import AutoModelForCausalLM, AutoTokenizer
#import torch

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and tokenizer
# try:
#     model_path = "deepseek-ai/deepseek-coder-1.3b-instruct"  # Adjust path as needed
#     tokenizer = AutoTokenizer.from_pretrained(model_path)
#     model = AutoModelForCausalLM.from_pretrained(
#         model_path,
#         torch_dtype=torch.float16,
#         device_map="auto",
#     )
# except Exception as e:
#     print(f"Error loading model: {e}")
#     model = None
#     tokenizer = None
#
class CodeRequest(BaseModel):
    code: str

@app.post("/analyze")
async def analyze_code(request: CodeRequest):
    # if model is None or tokenizer is None:
    #     raise HTTPException(status_code=500, detail="Model not loaded properly")
    #
    try:
        prompt = f"""Please analyze the following code and provide insights about its quality, potential issues, and suggestions for improvement:\n\n{request.code}\n\nAnalysis:"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-r1:7b",
                "prompt": prompt,
                "stream": False
            }
        )

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Ollama returned error: {response.text}")

        result = response.json()
        analysis = result.get("response", "").strip()
        # analysis = "Mock analysis result"
        return {"result": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}