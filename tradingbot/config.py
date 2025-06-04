import os
from dotenv import load_dotenv

load_dotenv()

SYMBOLS = os.getenv("SYMBOLS", "AAPL,TSLA").split(",")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RECOVERY_FILE = os.path.join(DATA_DIR, "recovery.json")
