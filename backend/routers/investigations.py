from fastapi import APIRouter
from lib.db import get_all

router = APIRouter()

@router.get("/")
def list_investigations():
    return get_all()
