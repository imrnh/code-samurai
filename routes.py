from fastapi import APIRouter, status
from models import UserModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from database import insert_into_db

api_routes = APIRouter(prefix="/api")


@api_routes.post("/")
async def create_user(user: UserModel):
    try:
        # insert_query = "INSERT INTO users (user_id, user_name, balance) VALUES (%s, %s, %s)"
        # insert_into_db(insert_query, (user.user_id, user.user_name, user.balance))

        return JSONResponse(content=jsonable_encoder(user), status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return JSONResponse(content=e, status_code=status.HTTP_400_BAD_REQUEST)