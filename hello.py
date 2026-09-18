import anthropic
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY from .env into the environment

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "In one sentence: what makes reconciling a bank statement against a ledger hard to fully automate?",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)