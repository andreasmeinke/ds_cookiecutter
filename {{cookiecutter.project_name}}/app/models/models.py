from pydantic import BaseModel, Field
from typing import Dict


class UserRequestIn(BaseModel):
    """This is the model for a user request please add elaborate description to all your models"""

    text: str = Field(...,
                     max_length=500,
                     description="This is a placeholder description, please configure."
                     )


class EntityOut(BaseModel):

    text: str = Field(...,
                     max_length=500,
                     description="This is a placeholder description, please configure."
                     )


class EntitiesOut(BaseModel):

    user_text_in: Dict[str, str] = Field(...,
                                         max_length=500,
                                         description="This is a placeholder description, please configure."
                                        )