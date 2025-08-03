# alx_travel_app_0x01

# ALX Travel App - API (alx_travel_app_0x01)

This Django-based project provides a RESTful API for managing property **listings** and **bookings** as part of a travel service platform. The project includes Swagger documentation for easy testing and exploration of endpoints.

## Features

- ✅ CRUD operations for:
  - Listings
  - Bookings
  - Properties
  - Property Types
  - Locations
  - Travel Destinations
- ✅ RESTful API with DRF (`ModelViewSet`)
- ✅ Swagger and Redoc documentation at `/swagger/` and `/redoc/`

## API Endpoints

All endpoints are available under `/api/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/listings/` | GET, POST | List or create a listing |
| `/api/listings/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a listing |
| `/api/bookings/` | GET, POST | List or create a booking |
| `/api/bookings/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a booking |
| `/api/property-types/` | ... | Manage property types |
| `/api/locations/` | ... | Manage locations |
| `/api/properties/` | ... | Manage property entries |
| `/api/destinations/` | GET | List all travel destinations |

## Setup Instructions

```bash
# Clone repo
git clone https://github.com/Macbeth111/alx_travel_app_0x01.git
cd alx_travel_app_0x01

# Create and activate virtual environment
python -m venv env
source env/Scripts/activate  # Windows

# Install dependencies
pip install -r requirement.txt

# Run the server
python manage.py runserver
