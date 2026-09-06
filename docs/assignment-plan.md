# Address Book Assignment Plan

## Goals

Build a FastAPI address book API where users can create, update, delete, and search addresses stored in SQLite.

## Principles

- TDD: write the smallest useful test first, then implement just enough code to pass it.
- SOLID: keep API, persistence, validation, and geospatial logic separated.
- CLEAN: prefer small, explicit modules with simple data flow and minimal coupling.

## Step 1: Foundations

Deliverables:

- Define the address domain model and request/response schemas.
- Validate address fields and coordinate ranges.
- Set up SQLite database session and ORM base.
- Add tests for address validation and model behavior.

Acceptance criteria:

- An address can be represented with coordinates and standard address fields.
- Invalid latitude or longitude is rejected.
- The project has a reusable database session layer for SQLite.

## Step 2: CRUD API

Status: complete.

Deliverables:

- Create address endpoints.
- Read single and multiple addresses.
- Update and delete addresses.

Acceptance criteria:

- Users can manage addresses through FastAPI Swagger.
- The API returns clear validation and not-found errors.

Notes:

- CRUD routes are implemented with a repository and service layer.
- The API is covered by a temporary SQLite integration test.

## Step 3: Nearby Search

Deliverables:

- Add an endpoint for addresses within a given radius of coordinates.
- Implement distance calculation in a dedicated service.

Acceptance criteria:

- Users can search by latitude, longitude, and distance.
- Results only include addresses within the requested radius.

## Step 4: Hardening

Deliverables:

- Add integration tests.
- Clean up API docs and examples.
- Review naming, structure, and separation of concerns.

Acceptance criteria:

- Core flows are tested.
- The code stays simple and maintainable.