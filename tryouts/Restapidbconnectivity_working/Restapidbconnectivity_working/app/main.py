from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from app.api.policy_routes import router as policy_router
from app.database import DATABASE_URL, database, metadata
from app.models.policy_model import policies  # noqa: F401 - registers table with metadata
from app.repository.policy_repositories import PolicyRepository
from app.services.policy_services import PolicyService


SEED_DATA = [
    {
        "name": "Life Secure Plus",
        "description": "Life insurance coverage for individuals and families",
        "maturity": "20 years",
        "premium": 1000.0,
    },
    {
        "name": "Health Protect",
        "description": "Health insurance policy covering hospitalization expenses",
        "maturity": "10 years",
        "premium": 1500.0,
    },
    {
        "name": "Child Future Plan",
        "description": "Savings and protection plan for a childs future",
        "maturity": "15 years",
        "premium": 800.0,
    },
    {
        "name": "Retirement Secure",
        "description": "Long term policy designed for retirement planning",
        "maturity": "25 years",
        "premium": 2000.0,
    },
    {
        "name": "Family Protection",
        "description": "Family focused life insurance protection plan",
        "maturity": "30 years",
        "premium": 2500.0,
    },
]


async def create_tables() -> None:
    engine = create_async_engine(DATABASE_URL)
    try:
        async with engine.begin() as connection:
            await connection.run_sync(metadata.create_all)
    finally:
        await engine.dispose()


async def seed_database() -> None:
    repository = PolicyRepository()
    if await repository.count() == 0:
        await repository.seed(SEED_DATA)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await database.connect()
    await seed_database()
    try:
        yield
    finally:
        await database.disconnect()


app = FastAPI(
    title="TFLInsurance REST API",
    description="Insurance Policy Management REST API using FastAPI and MySQL",
    version="1.0.0",
    lifespan=lifespan,
)

repository = PolicyRepository()
app.state.policy_service = PolicyService(repository)
app.include_router(policy_router)


@app.get("/")
async def home():
    return {
        "application": "TFLInsurance",
        "message": "TFLInsurance REST API is running",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
