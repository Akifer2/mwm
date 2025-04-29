from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session
from app.schemas import VehicleIn, VehicleOut
from app.crud import VehicleCRUD

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

@router.post("", response_model=VehicleOut, status_code=status.HTTP_201_CREATED)
async def create_vehicle(data: VehicleIn, session: AsyncSession = Depends(get_session)):
    return await VehicleCRUD(session).create(data.dict())

@router.get("/{vehicle_id}", response_model=VehicleOut)
async def read_vehicle(vehicle_id: int, session: AsyncSession = Depends(get_session)):
    vehicle = await VehicleCRUD(session).get(vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    return vehicle

@router.get("", response_model=list[VehicleOut])
async def list_vehicles(session: AsyncSession = Depends(get_session)):
    return await VehicleCRUD(session).list_all()

@router.put("/{vehicle_id}", response_model=VehicleOut)
async def update_vehicle(
    vehicle_id: int, data: VehicleIn, session: AsyncSession = Depends(get_session)
):
    vehicle = await VehicleCRUD(session).update(vehicle_id, data.dict())
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    return vehicle

@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vehicle(
    vehicle_id: int, session: AsyncSession = Depends(get_session)
):
    deleted = await VehicleCRUD(session).delete(vehicle_id)
    if not deleted:
        raise HTTPException(404, "Vehicle not found")
