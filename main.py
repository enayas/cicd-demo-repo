from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":
    "Make changes to this repo"
    "and.."
    "watch CI/CD in action!"}