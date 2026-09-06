from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.address import AddressCreate, AddressRead, AddressUpdate
from app.services.address_service import AddressService

router = APIRouter(prefix="/addresses", tags=["addresses"])


def get_address_service(db: Session = Depends(get_db)) -> AddressService:
    return AddressService(db)


@router.get("", response_model=list[AddressRead])
def list_addresses(service: AddressService = Depends(get_address_service)):
    return service.list_addresses()


@router.get("/{address_id}", response_model=AddressRead)
def get_address(address_id: int, service: AddressService = Depends(get_address_service)):
    address = service.get_address(address_id)
    if address is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    return address


@router.post("", response_model=AddressRead, status_code=status.HTTP_201_CREATED)
def create_address(payload: AddressCreate, service: AddressService = Depends(get_address_service)):
    return service.create_address(payload)


@router.patch("/{address_id}", response_model=AddressRead)
def update_address(
    address_id: int,
    payload: AddressUpdate,
    service: AddressService = Depends(get_address_service),
):
    address = service.update_address(address_id, payload)
    if address is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    return address


@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_address(address_id: int, service: AddressService = Depends(get_address_service)):
    deleted = service.delete_address(address_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
