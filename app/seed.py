import logging

from app.db.session import Base, SessionLocal, engine
from app.models.address import Address


logger = logging.getLogger(__name__)


DEFAULT_ADDRESSES: list[dict[str, object]] = [
    {
        "street": "Makati Avenue",
        "city": "Makati",
        "state": "Metro Manila",
        "postal_code": "1200",
        "country": "Philippines",
        "latitude": 14.5547,
        "longitude": 121.0244,
    },
    {
        "street": "Cebu IT Park",
        "city": "Cebu City",
        "state": "Cebu",
        "postal_code": "6000",
        "country": "Philippines",
        "latitude": 10.3289,
        "longitude": 123.9018,
    },
    {
        "street": "JP Laurel Avenue",
        "city": "Davao City",
        "state": "Davao del Sur",
        "postal_code": "8000",
        "country": "Philippines",
        "latitude": 7.0731,
        "longitude": 125.6128,
    },
    {
        "street": "Session Road",
        "city": "Baguio",
        "state": "Benguet",
        "postal_code": "2600",
        "country": "Philippines",
        "latitude": 16.4023,
        "longitude": 120.5960,
    },
]


def initialize_database(reset: bool = False) -> int:
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        if reset:
            logger.info("Resetting seeded database contents")
            db.query(Address).delete()
            db.commit()

        if db.query(Address).count() > 0:
            logger.info("Seed skipped because database already contains addresses")
            return 0

        db.add_all(Address(**address) for address in DEFAULT_ADDRESSES)
        try:
            db.commit()
        except Exception:
            db.rollback()
            logger.exception("Failed to seed starter addresses")
            raise

        logger.info("Seeded starter addresses", extra={"count": len(DEFAULT_ADDRESSES)})
        return len(DEFAULT_ADDRESSES)
    finally:
        db.close()
