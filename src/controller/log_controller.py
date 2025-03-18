from src.service.log_service import LogService

class LogController:
    def __init__(self, service: LogService = None):
        self.service = service if service is not None else LogService()

    def create_log(self, log_data: dict, token: str = None):
        return self.service.create_log(log_data, token=token)

    def get_log(self, log_id: str):
        return self.service.get_log(log_id)
