# FastAPI Booking

## Run

```bash
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/ to see the hello world response.

## Checks

```bash
./run-unit-tests
./run-checks
```

`run-unit-tests` runs the test suite only.
`run-checks` installs requirements and then runs the test suite.
`