from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":
    "Lets make changes and..."
    "watch CI/CD in action!!"}