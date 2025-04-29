from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Vehicle

class VehicleCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, data: dict) -> Vehicle:
        vehicle = Vehicle(**data)
        self.session.add(vehicle)
        await self.session.commit()
        await self.session.refresh(vehicle)
        return vehicle

    async def get(self, vehicle_id: int) -> Vehicle | None:
        res = await self.session.execute(
            select(Vehicle).where(Vehicle.id == vehicle_id)
        )
        return res.scalar_one_or_none()

    async def list_all(self) -> list[Vehicle]:
        res = await self.session.execute(select(Vehicle))
        return res.scalars().all()

    async def update(self, vehicle_id: int, data: dict) -> Vehicle | None:
        vehicle = await self.get(vehicle_id)
        if not vehicle:
            return None
        for key, value in data.items():
            setattr(vehicle, key, value)
        await self.session.commit()
        await self.session.refresh(vehicle)
        return vehicle

    async def delete(self, vehicle_id: int) -> bool:
        vehicle = await self.get(vehicle_id)
        if vehicle:
            await self.session.delete(vehicle)
            await self.session.commit()
            return True
        return False
