from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os, dotenv
from app.routes import router

dotenv.load_dotenv()
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app = FastAPI(title="Vehicle Service")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
