from pydantic import BaseModel
from typing import List, Dict


class AuditResponse(BaseModel):
    website: str
    health_score: int

    performance: Dict[str, str]

    seo: Dict[str, str]

    security: Dict[str, str]

    technical: Dict[str, int]

    recommendations: List[str]