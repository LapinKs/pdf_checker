from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
import uvicorn

app = FastAPI()

app.include_router(router)
app.mount("/main", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
