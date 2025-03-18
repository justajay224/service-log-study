import os
import redis
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

def get_redis_client():
    redis_uri = os.getenv("REDIS_URI")
    if not redis_uri:
        raise ValueError("REDIS_URI tidak ditemukan")

    client = redis.from_url(redis_uri)
    return client
