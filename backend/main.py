from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fact_check import fact_check
from nlp_processing import process_nlp
from image_generation import generate_infographic
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(input: InputText):
    text = input.text
    verdict, evidence = fact_check(text)
    topics, sentiment, entities = process_nlp(text)
    infographic = generate_infographic(text)
    return {
        "verdict": verdict,
        "evidence": evidence,
        "topics": topics,
        "sentiment": sentiment,
        "entities": entities,
        "infographic": infographic
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)