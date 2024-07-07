from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from app.database import engine, get_db

app = FastAPI()

origins = [
    "http://localhost:8080", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/feedback/", response_model=schemas.Feedback)
async def create_feedback(feedback: schemas.FeedbackCreate, db: AsyncSession = Depends(get_db)):
    new_feedback = models.Feedback(score=feedback.score)
    db.add(new_feedback)
    await db.commit()
    await db.refresh(new_feedback)
    return new_feedback