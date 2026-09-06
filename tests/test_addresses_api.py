from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.session import Base
from app.dependencies import get_db
from app.main import app


@pytest.fixture()
def client(tmp_path) -> Generator[TestClient, None, None]:
    database_path = tmp_path / "test_addresses.db"
    engine = create_engine(
        f"sqlite:///{database_path}",
        connect_args={"check_same_thread": False},
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db() -> Generator[Session, None, None]:
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def address_payload() -> dict[str, object]:
    return {
        "street": "123 Main St",
        "city": "Nairobi",
        "state": "Nairobi County",
        "postal_code": "00100",
        "country": "Kenya",
        "latitude": -1.286389,
        "longitude": 36.817223,
    }


def test_create_list_get_update_and_delete_address(client: TestClient, address_payload: dict[str, object]) -> None:
    create_response = client.post("/addresses", json=address_payload)

    assert create_response.status_code == 201
    created_address = create_response.json()
    assert created_address["id"] == 1
    assert created_address["city"] == "Nairobi"

    list_response = client.get("/addresses")

    assert list_response.status_code == 200
    assert list_response.json() == [created_address]

    get_response = client.get("/addresses/1")

    assert get_response.status_code == 200
    assert get_response.json() == created_address

    update_response = client.patch(
        "/addresses/1",
        json={"city": "Mombasa", "latitude": -4.043477},
    )

    assert update_response.status_code == 200
    updated_address = update_response.json()
    assert updated_address["city"] == "Mombasa"
    assert updated_address["latitude"] == -4.043477
    assert updated_address["street"] == "123 Main St"

    delete_response = client.delete("/addresses/1")

    assert delete_response.status_code == 204

    missing_response = client.get("/addresses/1")

    assert missing_response.status_code == 404
    assert missing_response.json()["detail"] == "Address not found"