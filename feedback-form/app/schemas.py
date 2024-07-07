from pydantic import BaseModel

class FeedbackBase(BaseModel):
    score: int

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int

    class Config:
        orm_mode = True
