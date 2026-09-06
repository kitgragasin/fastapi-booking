from app.seed import initialize_database
import os


if __name__ == "__main__":
    seeded_count = initialize_database(reset=os.getenv("FASTAPI_BOOKING_RESET_DB") == "1")
    print(f"Database initialized. Seeded {seeded_count} address(es).")
