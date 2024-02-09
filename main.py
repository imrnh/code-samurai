from app import app
import uvicorn
from database import create_tables


if __name__ == "__main__":
    # do anything that needs to be done before initiating the app
    create_tables()
    uvicorn.run("app:app", reload=True, host="0.0.0.0", port=8000, lifespan="on")