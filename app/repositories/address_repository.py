from sqlalchemy.orm import Session

from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate


class AddressRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def list(self) -> list[Address]:
        return self._db.query(Address).order_by(Address.id).all()

    def get(self, address_id: int) -> Address | None:
        return self._db.query(Address).filter(Address.id == address_id).first()

    def create(self, payload: AddressCreate) -> Address:
        address = Address(**payload.model_dump())
        self._db.add(address)
        self._db.commit()
        self._db.refresh(address)
        return address

    def update(self, address_id: int, payload: AddressUpdate) -> Address | None:
        address = self.get(address_id)
        if address is None:
            return None

        updates = payload.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(address, field, value)

        self._db.commit()
        self._db.refresh(address)
        return address

    def delete(self, address_id: int) -> bool:
        address = self.get(address_id)
        if address is None:
            return False

        self._db.delete(address)
        self._db.commit()
        return True
