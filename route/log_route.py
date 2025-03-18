from fastapi import APIRouter, Depends, HTTPException, Header
from src.controller.log_controller import LogController
from pydantic import BaseModel, Field
from typing import Optional, Dict

router = APIRouter()

# Model request untuk log
class LogData(BaseModel):
    level: str = Field(...)
    message: str = Field(...)
    metadata: Optional[Dict] = Field(default_factory=dict)

def get_log_controller():
    return LogController()

@router.post("/logs", response_model=dict)
def create_log(
    log: LogData,
    token: Optional[str] = Header(None),
    controller: LogController = Depends(get_log_controller)
    ):
    log_dict = log.dict()
    log_id = controller.create_log(log_dict, token=token)
    return {"log_id": log_id}

@router.get("/logs/{log_id}", response_model=dict)
def get_log(log_id: str, controller: LogController = Depends(get_log_controller)):
    
    log_entry = controller.get_log(log_id)
    if not log_entry:
        raise HTTPException(status_code=404, detail="Log tidak ditemukan")
    return log_entry
