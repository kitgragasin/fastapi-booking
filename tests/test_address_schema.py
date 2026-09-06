import pytest
from pydantic import ValidationError

from app.schemas.address import AddressCreate


def test_address_create_accepts_valid_coordinates() -> None:
    address = AddressCreate(
        street="123 Main St",
        city="Nairobi",
        state="Nairobi County",
        postal_code="00100",
        country="Kenya",
        latitude=-1.286389,
        longitude=36.817223,
    )

    assert address.latitude == pytest.approx(-1.286389)
    assert address.longitude == pytest.approx(36.817223)


@pytest.mark.parametrize(
    ("latitude", "longitude"),
    [
        (91, 36.8),
        (-91, 36.8),
        (-1.2, 181),
        (-1.2, -181),
    ],
)
def test_address_create_rejects_invalid_coordinates(latitude: float, longitude: float) -> None:
    with pytest.raises(ValidationError):
        AddressCreate(
            street="123 Main St",
            city="Nairobi",
            state="Nairobi County",
            postal_code="00100",
            country="Kenya",
            latitude=latitude,
            longitude=longitude,
        )