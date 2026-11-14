"""Pydantic v2 models for the IGNIS PSI fire-safety dashboard."""

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Variable(BaseModel):
    name: str
    values: str


class EnvScore(BaseModel):
    env_id: str
    score: int = Field(ge=0, le=100)
    rationale: str


class Investigation(BaseModel):
    id: str
    name: str
    full_name: str
    program: str
    hardware: str
    platform: str
    years: str
    status: str
    pillar: str
    gravity_levels: List[str]
    fuel_types: List[str]
    fuel_description: str
    objective: str
    test_conditions: str
    oxygen_min: Optional[float] = None
    oxygen_max: Optional[float] = None
    airflow: str
    variables: List[Variable] = []
    sensors: List[str] = []
    key_findings: List[str] = []
    si_summary: str
    earth_benefit: str
    env_scores: List[EnvScore] = []


class Environment(BaseModel):
    id: str
    label: str
    oxygen_pct: float
    pressure_psi: float
    gravity: str
    color: str


class OverviewStats(BaseModel):
    total_investigations: int
    by_pillar: Dict[str, int]
    by_status: Dict[str, int]
    fuel_types: List[str]
    oxygen_min: Optional[float] = None
    oxygen_max: Optional[float] = None
    hardware_platforms: List[str]
    environments: List[Environment]
    years_span: str


class Briefing(BaseModel):
    env_id: str
    title: str
    risk_profile: str
    top_investigation_ids: List[str] = []
    recommendations: List[str] = []
    gaps: List[str] = []
    engine: str = "si-synthesis-v1"
    generated_at: Optional[datetime] = None


class AskRequest(BaseModel):
    question: str
    environment: Optional[str] = None
    session_id: Optional[str] = None
