from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.models.address import Address
from app.repositories.address_repository import AddressRepository
from app.schemas.address import AddressCreate, AddressUpdate
from app.services.distance_service import DistanceService


@dataclass(frozen=True)
class NearbyAddress:
    address: Address
    distance_km: float


class AddressService:
    def __init__(self, db: Session) -> None:
        self._repository = AddressRepository(db)
        self._distance_service = DistanceService()

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

    def find_addresses_within_distance(
        self,
        latitude: float,
        longitude: float,
        distance_km: float,
    ) -> list[NearbyAddress]:
        addresses = self._repository.list()
        nearby_addresses: list[NearbyAddress] = []

        for address in addresses:
            address_distance = self._distance_service.haversine_km(
                latitude,
                longitude,
                address.latitude,
                address.longitude,
            )
            if address_distance <= distance_km:
                nearby_addresses.append(
                    NearbyAddress(address=address, distance_km=address_distance)
                )

        return sorted(nearby_addresses, key=lambda item: item.distance_km)
