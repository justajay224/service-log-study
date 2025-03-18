from datetime import datetime
from src.repository.log_repository import LogRepository
from database.redis_connection import get_redis_client

class LogService:
    def __init__(self, repository: LogRepository = None):
        self.repository = repository if repository is not None else LogRepository()

    def create_log(self, log_data: dict, token: str = None):
        if token:
            redis_client = get_redis_client()
            # Simpan token dengan key unik dan set TTL (misalnya 3600 detik = 1 jam)
            redis_client.set(f"token:{token}", token, ex=3600)
        
        log_data["created_at"] = datetime.utcnow().isoformat()
        return self.repository.insert_log(log_data)

    def get_log(self, log_id: str):
        return self.repository.find_log_by_id(log_id)
