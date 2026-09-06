import logging

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.address import AddressCreate, AddressRead, AddressUpdate
from app.services.address_service import AddressService

router = APIRouter(prefix="/addresses", tags=["addresses"])
logger = logging.getLogger(__name__)


def get_address_service(db: Session = Depends(get_db)) -> AddressService:
    return AddressService(db)


@router.get("", response_model=list[AddressRead])
def list_addresses(service: AddressService = Depends(get_address_service)):
    logger.debug("Listing addresses")
    return service.list_addresses()


@router.get("/{address_id}", response_model=AddressRead)
def get_address(address_id: int, service: AddressService = Depends(get_address_service)):
    address = service.get_address(address_id)
    if address is None:
        logger.warning("Address not found for lookup", extra={"address_id": address_id})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    logger.debug("Retrieved address", extra={"address_id": address_id})
    return address


@router.post("", response_model=AddressRead, status_code=status.HTTP_201_CREATED)
def create_address(payload: AddressCreate, service: AddressService = Depends(get_address_service)):
    address = service.create_address(payload)
    logger.info("Created address", extra={"address_id": address.id, "city": address.city, "country": address.country})
    return address


@router.patch("/{address_id}", response_model=AddressRead)
def update_address(
    address_id: int,
    payload: AddressUpdate,
    service: AddressService = Depends(get_address_service),
):
    address = service.update_address(address_id, payload)
    if address is None:
        logger.warning("Address not found for update", extra={"address_id": address_id})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    logger.info("Updated address", extra={"address_id": address_id})
    return address


@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_address(address_id: int, service: AddressService = Depends(get_address_service)):
    deleted = service.delete_address(address_id)
    if not deleted:
        logger.warning("Address not found for delete", extra={"address_id": address_id})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found")
    logger.info("Deleted address", extra={"address_id": address_id})
    return Response(status_code=status.HTTP_204_NO_CONTENT)
