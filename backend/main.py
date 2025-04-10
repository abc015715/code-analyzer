# ../backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
    #     # Prepare prompt
    #     prompt = f"""Please analyze the following code and provide insights about its quality, potential issues, and suggestions for improvement:
    #
    #     {request.code}
    #
    #     Analysis:"""
    #
    #     # Generate response
    #     inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    #     outputs = model.generate(
    #         **inputs,
    #         max_length=1000,
    #         temperature=0.7,
    #         do_sample=True,
    #         pad_token_id=tokenizer.eos_token_id
    #     )
    #
    #     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    #
    #     # Extract the analysis part (after "Analysis:")
    #     analysis = response.split("Analysis:")[-1].strip()
        analysis = "Mock analysis result"
        return {"result": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}