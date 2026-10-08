from app.database import database
from app.models.policy_model import policies


class PolicyRepository:
    async def get_all(self):
        rows = await database.fetch_all(policies.select())
        return [dict(row._mapping) for row in rows]

    async def get_by_id(self, policy_id: int):
        query = policies.select().where(policies.c.id == policy_id)
        row = await database.fetch_one(query)
        return None if row is None else dict(row._mapping)

    async def create(self, policy_data: dict):
        query = policies.insert().values(**policy_data)
        policy_id = await database.execute(query)
        return {"id": policy_id, **policy_data}

    async def update(self, policy_id: int, policy_data: dict):
        query = (
            policies.update()
            .where(policies.c.id == policy_id)
            .values(**policy_data)
        )
        result = await database.execute(query)
        if result == 0:
            return None
        return {"id": policy_id, **policy_data}

    async def delete(self, policy_id: int) -> bool:
        query = policies.delete().where(policies.c.id == policy_id)
        result = await database.execute(query)
        return result > 0

    async def count(self) -> int:
        query = "SELECT COUNT(*) FROM policies"
        result = await database.fetch_val(query)
        return int(result or 0)

    async def seed(self, seed_data: list[dict]) -> None:
        query = policies.insert()
        await database.execute_many(query, seed_data)
