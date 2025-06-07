import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_claims(text):
    return [text]

def verify_claims(claims):
    GOOGLE_API_KEY = os.getenv("AIzaSyBrSVqKsw6CmzLv8LylYBjgEMQzTG4JJn8")
    SEARCH_ENGINE_ID = os.getenv("c63a926e674c641c0")
    search_url = "https://www.googleapis.com/customsearch/v1"

    for claim in claims:
        params = {"key": GOOGLE_API_KEY, "cx": SEARCH_ENGINE_ID, "q": claim, "num": 5}
        try:
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            results = response.json().get("items", [])
            evidence = [result["snippet"] for result in results]
            verdict = "Unverified" if not evidence else "True"
            return verdict, " ".join(evidence)
        except Exception as e:
            return "Unverified", f"Error: {str(e)}"

def fact_check(text):
    claims = extract_claims(text)
    verdict, evidence = verify_claims(claims)
    return verdict, evidence