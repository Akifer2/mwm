import asyncio
from app.db import async_session, engine, Base
from app.models import Vehicle

vehicles = [
    {"plate": "AAA1B23", "brand": "Ford",      "model": "Ranger", "year": 2021, "color": "Blue"},
    {"plate": "BBB4C56", "brand": "Chevrolet", "model": "S10",    "year": 2022, "color": "White"},
]

async def run():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)   # garante a tabela

    async with async_session() as session:
        session.add_all(Vehicle(**v) for v in vehicles)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(run())
