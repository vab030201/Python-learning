from sqlalchemy import Column, Float, Integer, String, Table
from app.database import metadata

policies = Table(
    "policies",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("description", String(255), nullable=False),
    Column("maturity", String(50), nullable=False),
    Column("premium", Float, nullable=False),
)
