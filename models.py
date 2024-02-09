from pydantic import BaseModel

class UserModel(BaseModel):
    user_id : int
    user_name: str
    balance : int