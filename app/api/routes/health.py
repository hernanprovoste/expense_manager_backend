from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Health"])
def read_root():
    return {"message": "API is running"}