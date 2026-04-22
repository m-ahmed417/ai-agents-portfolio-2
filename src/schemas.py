from pydantic import BaseModel, Field 
from typing import Literal


class TicketRoute(BaseModel):
    category: Literal["billing", "bug", "how_to", "other", "feature_request", "account_access"]
    urgency: Literal["low", "medium", "high", "critical"]
    missing_information: list[str] = Field(default_factory=list)
    suggested_next_action: str = Field(min_length=1)
    confidence: float = Field(ge=0, le=1)
    
class GoldenExpected(BaseModel): 
    category: Literal["account_access", "billing", "bug", "how_to", "feature_request", "other"]
    urgency: Literal["low", "medium", "high", "critical"]
    missing_information: list[str] = Field(default_factory=list)
    suggested_next_action: str = Field(min_length=1)
    
class GoldenFixture(BaseModel):
    id: str
    message: str = Field(min_length=1)
    expected: GoldenExpected
    notes: str = Field(min_length=1)
    


