from fastapi import FastAPI
# import graphene

from app.routers import bull
from app.routers import proof
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bull.router)
app.include_router(proof.router)

@app.get("/")
async def root():
    return {"message": "WWS API root."}