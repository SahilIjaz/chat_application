import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set in environment")

client = Groq(api_key=api_key)

def run_llm_agent(message: str):
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return {
            "reply": completion.choices[0].message.content
        }
    except Exception as e:
        print(f"LLM Agent Error: {str(e)}")
        raise
