import anthropic
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Connect to Claude
client = anthropic.Anthropic()

# Send a test message
message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Hello Claude! Introduce yourself in one sentence."}
    ]
)

# Display Claude's reply
for block in message.content:
    if block.type == "text":
        print(block.text)