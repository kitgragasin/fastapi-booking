from sqlalchemy.orm import Session

from app.repositories.address_repository import AddressRepository
from app.schemas.address import AddressCreate, AddressUpdate


class AddressService:
    def __init__(self, db: Session) -> None:
        self._repository = AddressRepository(db)

    def list_addresses(self):
        return self._repository.list()

    def get_address(self, address_id: int):
        return self._repository.get(address_id)

    def create_address(self, payload: AddressCreate):
        return self._repository.create(payload)

    def update_address(self, address_id: int, payload: AddressUpdate):
        return self._repository.update(address_id, payload)

    def delete_address(self, address_id: int) -> bool:
        return self._repository.delete(address_id)
