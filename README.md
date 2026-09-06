# FastAPI Booking

## Run

```bash
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/ to see the hello world response.
Open http://127.0.0.1:8000/docs to use FastAPI's Swagger UI.

## Nearby Search

Use the nearby endpoint to return addresses within a radius (in kilometers), sorted by nearest first.

```bash
GET /addresses/nearby?latitude=14.5995&longitude=120.9842&distance_km=300
```

### 5 km Examples

Try these in Swagger to see clustered results from the seeded data:

```bash
GET /addresses/nearby?latitude=14.5547&longitude=121.0244&distance_km=5
GET /addresses/nearby?latitude=16.4023&longitude=120.5960&distance_km=5
```

- The Makati query should return at least 4 places.
- The Baguio query should return at least 5 places.

## Checks

```bash
./run-unit-tests
./run-checks
./init-db
```

`run-unit-tests` runs the test suite only.
`run-checks` installs requirements and then runs the test suite.
`init-db` creates the SQLite database and seeds a few starter addresses.