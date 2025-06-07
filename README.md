# AI Fact-Check & Multimedia Generator

A web platform for fact-checking news or social media posts, performing NLP analysis, and generating AI visuals.

## Architecture
- **Frontend**: React for interactive UI
- **Backend**: FastAPI for API endpoints
- **NLP**: Hugging Face Transformers and spaCy for claim extraction, sentiment, and NER
- **Fact-Checking**: Bing API for evidence search
- **Image Generation**: Stable Diffusion for infographics
- **Deployment**: Suitable for Vercel (frontend) and Render (backend)

## Setup Instructions
1. **Backend**:
   - Navigate to `backend/`
   - Install dependencies: `pip install -r requirements.txt`
   - Replace `YOUR_BING_API_KEY` in `fact_check.py` and `YOUR_HF_TOKEN` in `image_generation.py`
   - Run: `uvicorn main:app --host 0.0.0.0 --port 8000`

2. **Frontend**:
   - Navigate to `frontend/`
   - Install dependencies: `npm install`
   - Run: `npm start`

3. Access the app at `http://localhost:3000`

## Notes
- Replace API keys in `backend/fact_check.py` and `backend/image_generation.py`.
- Enhance frontend styling in `frontend/src/styles.css` for better UI/UX.
- Ensure CORS is configured for your deployment domain.

## Rubric Coverage
- Claim Verification: Bing API search
- NLP Processing: Sentiment, NER, and topic classification
- GenAI Visuals: Stable Diffusion infographic
- UI/UX: Basic React interface
- Deployment: Ready for Vercel/Render
- Docs: This README