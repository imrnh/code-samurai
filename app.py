from fastapi import FastAPI, Request, Depends, File, UploadFile, HTTPException, status, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from datetime import datetime, timedelta, timezone
from typing import Annotated

from routes import api_routes


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.middleware("http")
async def middleware_1(request: Request, call_next):
    print("I'm middleware")
    response = await call_next(request)
    return response


app.include_router(api_routes)