# ai-fact-check-2

AI Fact-Checker
AI Fact-Checker is a full-stack web application that analyzes claims using natural language processing (NLP) and generates infographics to summarize findings. The frontend is built with React and styled using Tailwind CSS with custom styles, while the backend uses FastAPI to perform fact-checking and image generation with Google Custom Search and Hugging Face APIs.
Features

Claim Analysis: Input a claim (e.g., "The moon is made of cheese") to get a verdict, evidence, topics, sentiment, and entities.
Infographic Generation: Automatically creates visual summaries of analysis results.
Responsive Design: Modern UI with a clean, card-based layout, optimized for desktop and mobile.
Error Handling: Displays user-friendly error and loading messages.
API Integration: Connects to a FastAPI backend for real-time processing.

Tech Stack

Frontend: React 18, Tailwind CSS 3.4.1, Custom CSS
Backend: FastAPI, Google Custom Search API, Hugging Face (Stable Diffusion)
Tools: Node.js 18.x, npm, Vercel (deployment), Git

Prerequisites

Node.js: Version 18.x (download from nodejs.org)
Python: Version 3.9+ (for backend)
Git: For cloning the repository
API Keys:
Google Custom Search API Key and Search Engine ID (Google Cloud Console)
Hugging Face Token (Hugging Face)



Installation
Frontend

Clone the Repository:
git clone https://github.com/your-username/ai-fact-checker.git
cd ai-fact-checker/frontend


Install Dependencies:
npm install


Run Development Server:
npm start


The app will run at http://localhost:3000.


Build for Production:
npm run build


Output is in the build folder.



Backend

Navigate to Backend:
cd ../backend


Create Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate


Install Dependencies:
pip install fastapi uvicorn python-dotenv google-api-python-client transformers torch


Set Environment Variables:

Create a .env file in backend/:echo "GOOGLE_API_KEY=your_google_api_key" > .env
echo "SEARCH_ENGINE_ID=your_search_engine_id" >> .env
echo "HF_TOKEN=your_hugging_face_token" >> .env




Run Backend Server:
uvicorn main:app --host 0.0.0.0 --port 8000


API will be available at http://localhost:8000.



Usage

Open the App: Navigate to http://localhost:3000 in your browser.
Enter a Claim: Type a claim (e.g., "The moon is made of cheese") in the textarea.
Analyze: Click "Analyze Claim" to get results, including:
Verdict: True or Unverified
Evidence: Supporting information from web searches
Topics: Key topics extracted
Sentiment: Positive, Negative, or Neutral
Entities: Named entities identified
Infographic: Visual summary (if generated successfully)


Download Infographic: Click the download link to save the image.

Deployment
Frontend (Vercel)

Push to GitHub:
git add .
git commit -m "Initial commit"
git push origin main


Connect to Vercel:

Go to Vercel, sign in, and click "New Project".
Import your GitHub repository.
Configure:
Framework Preset: Create React App
Build Command: CI=false npm run build
Output Directory: build
Node.js Version: 18.x (Settings → General → Node.js Version)


Deploy.


Troubleshooting:

If you see Could not find index.html:
Ensure public/index.html exists.
Verify npm run build generates build/index.html locally.
Add vercel.json:{
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": { "distDir": "build" }
    }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "/index.html" }
  ]
}







Backend

Deploy to a platform like Render or Vercel Serverless Functions.
Update App.js to use the deployed backend URL:const response = await fetch('https://your-backend-url/analyze', {



Project Structure
ai-fact-checker/
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   ├── manifest.json
│   ├── src/
│   │   ├── components/
│   │   │   ├── InputForm.js
│   │   │   ├── ResultsDashboard.js
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── index.css
│   ├── package.json
│   ├── tailwind.config.js
│   ├── vercel.json
├── backend/
│   ├── main.py
│   ├── fact_check.py
│   ├── nlp_processing.py
│   ├── image_generation.py
│   ├── .env
├── README.md

Styling

Tailwind CSS: Utility classes for responsive design (e.g., text-3xl, bg-gray-100).
Custom CSS: Defined in frontend/src/index.css with classes like .app, .input-form, .submit-button for a modern, card-based UI with shadows, gradients, and hover effects.

Troubleshooting

Styles Not Applied:
Run npx tailwindcss -i ./src/index.css -o ./src/output.css --watch.
Ensure index.css is imported in index.js.
Check browser console (F12) for CSS errors.


Vercel Build Fails:
Set CI=false in build command.
Verify public/index.html and build output.
Check Vercel logs for specific errors (e.g., Module not found).


Backend Errors:
Validate API keys in .env.
Test API at http://localhost:8000/docs.



Contributing

Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit changes: git commit -m "Add feature".
Push to branch: git push origin feature-name.
Open a Pull Request.

License
MIT License. See LICENSE for details.

