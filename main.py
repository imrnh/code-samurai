from app import app
import uvicorn


if __name__ == "__main__":
    # do anything that needs to be done before initiating the app

    uvicorn.run("app:app", reload=True, port=8000, lifespan="on")