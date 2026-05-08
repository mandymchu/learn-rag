import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY      = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL     = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_CHAT_MODEL   = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
OPENAI_EMBED_MODEL  = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


def check_config():
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set. Check your .env file.")
    print(f"✅ Config loaded")
    print(f"   model : {OPENAI_CHAT_MODEL}")
    print(f"   embed : {OPENAI_EMBED_MODEL}")
    print(f"   base  : {OPENAI_BASE_URL}")


if __name__ == "__main__":
    check_config()
