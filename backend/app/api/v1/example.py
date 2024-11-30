from fastapi import APIRouter, status

router = APIRouter(prefix="/example", tags=["Example"])


# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create(model: example):  
#     return await example.create(model)