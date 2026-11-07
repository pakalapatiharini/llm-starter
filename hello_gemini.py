
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Connect to Gemini
client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain Python in simple words."
    )

    print("\nGemini's Response:")
    print(response.text)

except Exception as error:
    print("\nSomething went wrong:")
    print(error)
