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

## Checks

```bash
./run-unit-tests
./run-checks
./init-db
```

`run-unit-tests` runs the test suite only.
`run-checks` installs requirements and then runs the test suite.
`init-db` creates the SQLite database and seeds a few starter addresses.
`