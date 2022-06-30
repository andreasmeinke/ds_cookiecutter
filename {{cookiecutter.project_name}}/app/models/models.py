from pydantic import BaseModel
from typing import List, Dict
from enum import Enum


class UserRequestIn(BaseModel):
    """This is the model for a user request"""

    text: str


class EntityOut(BaseModel):

    text: str


class EntitiesOut(BaseModel):

    user_text_in: Dict[str]