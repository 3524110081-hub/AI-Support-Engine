
from typing import Literal

from pydantic import BaseModel


class SupportResponse(BaseModel):
    category: Literal["ACCESS", "BUG", "FEATURE", "SECURITY"]
    priority: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    response: str
    requiresHumanReview: bool
    mode: Literal["traditional", "generative"]