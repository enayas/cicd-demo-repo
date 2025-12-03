from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":
    "Push changes to this "
    "connected repo and..."
    "watch CI/CD in action!"}