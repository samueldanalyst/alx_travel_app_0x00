ALX Travel App
A Django REST Framework API for managing travel listings, bookings, and reviews.
Includes user authentication integration with Django’s built-in User model.

Table of Contents
Project Overview

Features

Tech Stack

Installation

Usage

API Endpoints

Models

Contributing

License

Project Overview
This project provides an API backend for a travel booking application where users can list properties, book them, and leave reviews. The API supports CRUD operations for listings, bookings, and reviews, and integrates user accounts.

Features
Create, read, update, and delete Listings, Bookings, and Reviews

User association with listings and bookings

Auto-generated API documentation via Swagger

Ready for future authentication and permission customization

Tech Stack
Python 3.13

Django 5.2.1

Django REST Framework

drf-yasg for Swagger API documentation

SQLite (default, can be switched)

Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/alx-travel-app.git
cd alx-travel-app
Create and activate a virtual environment

bash
Copy
Edit
python -m venv env
# Windows
.\env\Scripts\activate
# macOS/Linux
source env/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py migrate
Create a superuser (for admin access)

bash
Copy
Edit
python manage.py createsuperuser
Run the development server

bash
Copy
Edit
python manage.py runserver
Usage
Access the admin panel: http://127.0.0.1:8000/admin/

API root endpoint: http://127.0.0.1:8000/api/

Swagger API docs: http://127.0.0.1:8000/swagger/

API Endpoints
Endpoint	Methods	Description
/api/listings/	GET, POST	List all listings or create one
/api/listings/{id}/	GET, PUT, DELETE	Retrieve, update or delete a listing
/api/bookings/	GET, POST	List all bookings or create one
/api/bookings/{id}/	GET, PUT, DELETE	Retrieve, update or delete a booking
/api/reviews/	GET, POST	List all reviews or create one
/api/reviews/{id}/	GET, PUT, DELETE	Retrieve, update or delete a review

Models
Listing
listing_id (AutoField, primary key)

lister (ForeignKey to User)

title (CharField)

description (TextField)

location (CharField)

price (DecimalField)

Booking
booking_id (AutoField, primary key)

booked_by (ForeignKey to User)

booking_date (DateField, auto set on create)

listing (ForeignKey to Listing)

Review
review_id (AutoField, primary key)

listing (ForeignKey to Listing)

booking (ForeignKey to Booking)

created_at (DateField, auto updated on save)

comment (TextField)

review_rating (IntegerField)

Contributing
Contributions are welcome! Please fork the repo and create a pull request with your feature or bug fix.
