from fastapi import APIRouter, Query
from app.utils import classify_number

router = APIRouter()

@router.get("/api/classify-number")
def get_number_info(number: int = Query(..., description="Number to classify")):
    return classify_number(number)
