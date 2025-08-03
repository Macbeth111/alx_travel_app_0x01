# ALX Travel App 0x01

This Django REST API manages travel listings and bookings. The API supports CRUD operations on models like Listing, Booking, Property, Location, and more.

## API Base URL

All endpoints are served under /api/

## Main Endpoints

- /api/listings/ - CRUD for travel listings
- /api/bookings/ - CRUD for travel bookings
- /api/property-types/ - Manage property types
- /api/locations/ - Manage travel locations
- /api/properties/ - Manage property details
- /api/destinations/ - List available travel destinations

## API Documentation

- Swagger UI: http://localhost:8000/swagger/
- Redoc: http://localhost:8000/redoc/

## Setup Instructions

\\\ash
git clone https://github.com/Macbeth111/alx_travel_app_0x01.git
cd alx_travel_app_0x01

python -m venv env
source env/Scripts/activate  # For Windows

pip install -r requirements.txt

python manage.py runserver
\\\

## Author

Macbeth Obimpeh

<<<<<<< HEAD
This project contains Django models, serializers, and seed data for a travel application built as part of the ALX Backend specialization.
# ALX Travel App - Phase 0

## Overview

This Django-based application is part of the ALX backend specialization. It allows users to view travel listings, make bookings, and leave reviews. This version focuses on setting up the database, serializers, and seeding sample data.

## Features

- Define and manage models for:
  - Listings
  - Bookings
  - Reviews
- RESTful API with serializers for Listings and Bookings
- Custom management command to seed sample data into the database
- Swagger UI for API testing

## Technologies Used

- Django
- Django REST Framework
- SQLite3 (default DB for development)
- Swagger / drf-yasg

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/alx_travel_app_0x00.git
   cd alx_travel_app_0x00
   ```
=======
>>>>>>> 83d50d6 (Add final README for project visibility)
