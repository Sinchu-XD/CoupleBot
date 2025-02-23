import os


API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
