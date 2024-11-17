from pydantic import BaseModel

class ASGTag(BaseModel):
    Key: str
    Value: str
