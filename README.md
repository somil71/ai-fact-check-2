# AI Fact-Check & Multimedia Generator

🧠 AI Fact-Checker & Multimedia Generator

A cutting-edge web platform powered by AI to verify claims from news or social media, perform NLP analysis, and generate engaging infographics or narrated videos. Built with a modern tech stack, it offers a sleek, responsive UI and robust backend processing.

  


📑 Table of Contents

Features
Tech Stack
Prerequisites
Installation
Usage
Development
Deployment
Rubric Mapping
Troubleshooting
Contributing
License
Resources

✨ Features

Claim Verification: Extracts and validates claims using Bing Search API.
NLP Analysis: Performs topic classification, sentiment analysis, and named entity recognition (NER) with Hugging Face Transformers and spaCy.
Visual Generation: Creates infographics using Stable Diffusion via Diffusers.
Optional Video Summaries: Generates narrated videos with Coqui TTS and Text2Video (bonus feature).
Interactive Dashboard: Displays results with verdicts, evidence, sources, and visuals in a modern UI.
Responsive Design: Optimized for desktop and mobile with Tailwind CSS and custom styles.

🛠 Tech Stack



Component
Technology



Frontend
React (Vite), Tailwind CSS, Custom CSS


Backend
FastAPI, Python 3.9+


NLP
Hugging Face Transformers, spaCy


Fact-Checking
Bing Search API


Visual Generation
Stable Diffusion (Diffusers)


Video (Optional)
Coqui TTS, Text2Video


Deployment
Vercel (Frontend), Render (Backend)


📋 Prerequisites

Node.js: 18.x (Download)
Python: 3.9+ (Download)
Git: For cloning (Download)
API Keys:
Bing Search API Key (Azure Portal)
Hugging Face Token (Hugging Face)



🔧 Installation
1. Clone the Repository
git clone https://github.com/your-username/ai-fact-checker.git
cd ai-fact-checker

2. Backend Setup

Navigate to backend:cd backend


Create a virtual environment:python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\Activate


Install dependencies:pip install fastapi uvicorn python-dotenv bing-search-api transformers spacy torch diffusers
pip install coqui-tts text2video  # Optional for video
python -m spacy download en_core_web_sm


Configure environment variables:
Create .env:echo "BING_API_KEY=your_bing_api_key" > .env
echo "HF_TOKEN=your_hugging_face_token" >> .env




Run the backend:uvicorn main:app --host 0.0.0.0 --port 8000


Access API docs at http://localhost:8000/docs.



3. Frontend Setup

Navigate to frontend:cd ../frontend


Install dependencies:npm install


Run development server:npm run dev


Open http://localhost:3000 (Vite default port).


Build for production:npm run build


Output is in dist/.



📖 Usage

Open http://localhost:3000 or the deployed URL.
Enter a URL or text claim (e.g., "The moon is made of cheese").
Click "Analyze" button to process:
Verdict: True, False, or Unverified
Evidence: Web search results
NLP: Topics, sentiment, entities
Visuals: Infographic image
Optional: Narrated video


View results in the interactive dashboard with downloadable visuals.

💻 Development

Customize Styles: Edit frontend/src/index.css for Tailwind or custom styles.
CORS: Ensure backend allows frontend domains in backend/main.py:from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-vercel-url"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Infographic Prompts: Modify backend/image_generation.py.
Claim Logic: Tweak backend/fact_check.py.
Video Generation: Implement in backend/video/ (optional).

🚀 Deployment
Frontend (Vercel)

Push to GitHub:git add .
git commit -m "Deploy frontend"
git push origin main


Deploy on Vercel:
Import repository in Vercel Dashboard.
Configure:
Framework Preset: Vite
Build Command: npm run build
Output Directory: dist
Node.js Version: 18.x
Environment Variables: Add backend URL if needed.


Create vercel.json:{
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": { "distDir": "dist" }
    }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "/index.html" }
  ]
}




Fix index.html Error:
Ensure frontend/public/index.html exists:<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AI Fact-Checker</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>


Verify npm run build generates dist/index.html.



Backend (Render)

Create a new Web Service on Render.
Configure:
Repository: Your GitHub repo (backend/).
Runtime: Python 3.
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
Environment Variables: Add BING_API_KEY, HF_TOKEN.


Deploy and update frontend/src/App.js:const response = await fetch('https://your-render-url/analyze', {



✅ Rubric Mapping



Requirement
Covered



✅ Claim Verification
Bing Search API


✅ NLP Analysis
Transformers, spaCy


✅ AI Visuals
Stable Diffusion


✅ UI/UX
React, Tailwind CSS


✅ Deployment
Vercel, Render


✅ Documentation
README, Project Report PDF


🔁 Bonus Video (Optional)
Coqui TTS, Text2Video


🛠 Troubleshooting

Vercel index.html Error:
Run npm run build locally to check dist/index.html.
Ensure public/index.html exists.
Verify vercel.json and Vite config (vite.config.js).


Styles Not Applied:
Run npx tailwindcss -i ./src/index.css -o ./src/output.css --watch.
Check index.js imports index.css.
Inspect browser console (F12).


Backend API Errors:
Validate BING_API_KEY and HF_TOKEN.
Test API: curl -X POST -d '{"text":"test"}' http://localhost:8000/analyze.


Build Fails:
Set CI=false npm run build in Vercel.
Check Node.js 18.x compatibility.



🤝 Contributing

Fork the repository.
Create a branch: git checkout -b feature/your-feature.
Commit changes: git commit -m "Add feature".
Push: git push origin feature/your-feature.
Open a Pull Request.

📄 License
MIT License
📚 Resources

Project Report PDF
Vite Documentation
FastAPI Documentation
Tailwind CSS Documentation

[AI_FactCheck_Project_Instructions_Clean.pdf](https://github.com/user-attachments/files/20637253/AI_FactCheck_Project_Instructions_Clean.pdf)
