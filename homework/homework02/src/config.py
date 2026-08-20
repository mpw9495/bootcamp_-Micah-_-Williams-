import os
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    """Load environment variables from the project's .env file."""
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(env_path)


def get_key(key, default=None):
    """Return an environment variable by name."""
    return os.getenv(key, default)
