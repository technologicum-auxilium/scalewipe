from fastapi import APIRouter, HTTPException
from src.app.controllers.asf_controller import update_asg
from src.app.models import asg_model
from . import app

router = APIRouter()

@router.post("/update-asg")
async def handle_update_asg(tag: asg_model.ASGTag):
    result = update_asg(tag)
    return result

app.include_router(router)
