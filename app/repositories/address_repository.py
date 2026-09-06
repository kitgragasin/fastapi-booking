import logging

from sqlalchemy.orm import Session

from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate


logger = logging.getLogger(__name__)


class AddressRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def list(self) -> list[Address]:
        logger.debug("Loading all addresses from database")
        return self._db.query(Address).order_by(Address.id).all()

    def get(self, address_id: int) -> Address | None:
        logger.debug("Loading address by id", extra={"address_id": address_id})
        return self._db.query(Address).filter(Address.id == address_id).first()

    def create(self, payload: AddressCreate) -> Address:
        address = Address(**payload.model_dump())
        self._db.add(address)
        try:
            self._db.commit()
            self._db.refresh(address)
        except Exception:
            self._db.rollback()
            logger.exception("Failed to create address")
            raise

        logger.debug("Address persisted", extra={"address_id": address.id})
        return address

    def update(self, address_id: int, payload: AddressUpdate) -> Address | None:
        address = self.get(address_id)
        if address is None:
            return None

        updates = payload.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(address, field, value)

        try:
            self._db.commit()
            self._db.refresh(address)
        except Exception:
            self._db.rollback()
            logger.exception("Failed to update address", extra={"address_id": address_id})
            raise

        logger.debug("Address updated", extra={"address_id": address_id})
        return address

    def delete(self, address_id: int) -> bool:
        address = self.get(address_id)
        if address is None:
            return False

        self._db.delete(address)
        try:
            self._db.commit()
        except Exception:
            self._db.rollback()
            logger.exception("Failed to delete address", extra={"address_id": address_id})
            raise

        logger.debug("Address deleted", extra={"address_id": address_id})
        return True
