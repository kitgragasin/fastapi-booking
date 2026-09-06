from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.seed as seed_module
from app.db.session import Base
from app.models.address import Address


def test_initialize_database_seeds_addresses_once(tmp_path, monkeypatch) -> None:
    database_path = tmp_path / "seed.db"
    engine = create_engine(
        f"sqlite:///{database_path}",
        connect_args={"check_same_thread": False},
    )
    testing_session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    monkeypatch.setattr(seed_module, "engine", engine)
    monkeypatch.setattr(seed_module, "SessionLocal", testing_session_local)
    monkeypatch.setattr(seed_module, "Base", Base)

    seeded_count = seed_module.initialize_database()

    assert seeded_count == len(seed_module.DEFAULT_ADDRESSES)

    with testing_session_local() as db:
        assert db.query(Address).count() == len(seed_module.DEFAULT_ADDRESSES)

    assert seed_module.initialize_database() == 0


def test_initialize_database_reset_reseeds_addresses(tmp_path, monkeypatch) -> None:
    database_path = tmp_path / "seed-reset.db"
    engine = create_engine(
        f"sqlite:///{database_path}",
        connect_args={"check_same_thread": False},
    )
    testing_session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    monkeypatch.setattr(seed_module, "engine", engine)
    monkeypatch.setattr(seed_module, "SessionLocal", testing_session_local)
    monkeypatch.setattr(seed_module, "Base", Base)

    assert seed_module.initialize_database() == len(seed_module.DEFAULT_ADDRESSES)

    with testing_session_local() as db:
        db.query(Address).delete()
        db.commit()
        assert db.query(Address).count() == 0

    assert seed_module.initialize_database(reset=True) == len(seed_module.DEFAULT_ADDRESSES)

    with testing_session_local() as db:
        assert db.query(Address).count() == len(seed_module.DEFAULT_ADDRESSES)
