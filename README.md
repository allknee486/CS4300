# Movie Booking System

A Django REST Framework-based API for managing movie bookings, seat reservations, and viewing schedules.

## Features

- **Movie Management**: Create, read, update, and delete movie listings
- **Seat Management**: View seat availability and manage seat reservations
- **Booking System**: Create bookings and view booking history
- **RESTful API**: Well-structured endpoints following REST principles
- **Django Admin**: Easy-to-use admin interface for management

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie-booking-system
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

Deployment
This project is deployed on Render, a cloud platform for hosting web applications.
Live Application

Production URL: https://your-app-name.onrender.com/api/
Admin Panel: https://your-app-name.onrender.com/admin/

Deploying to Render
Prerequisites

A Render account (sign up at render.com)
Your project pushed to a Git repository (GitHub, GitLab, or Bitbucket)

## API Endpoints

### Movies
- `GET /api/movies/` - List all movies
- `POST /api/movies/` - Create a new movie
- `GET /api/movies/{id}/` - Retrieve a specific movie
- `PUT /api/movies/{id}/` - Update a movie
- `PATCH /api/movies/{id}/` - Partially update a movie
- `DELETE /api/movies/{id}/` - Delete a movie

### Seats
- `GET /api/seats/` - List all seats
- `POST /api/seats/` - Create a new seat
- `GET /api/seats/{id}/` - Retrieve a specific seat
- `PUT /api/seats/{id}/` - Update seat information
- `DELETE /api/seats/{id}/` - Delete a seat

### Bookings
- `GET /api/bookings/` - List all bookings (booking history)
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/{id}/` - Retrieve a specific booking
- `PUT /api/bookings/{id}/` - Update a booking
- `DELETE /api/bookings/{id}/` - Cancel a booking

## Usage Examples

### Create a Movie
```bash
curl -X POST http://localhost:8000/api/movies/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Inception",
    "description": "A mind-bending thriller",
    "duration": 148,
    "release_date": "2010-07-16"
  }'
```

### Check Available Seats
```bash
curl http://localhost:8000/api/seats/
```

### Create a Booking
```bash
curl -X POST http://localhost:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -d '{
    "movie": 1,
    "seat": 5,
    "customer_name": "John Doe",
    "customer_email": "john@example.com"
  }'
```

## Project Structure

```
CS4300/
  render.yaml
  movie-booking-system/
  ├── manage.py
  ├── requirements.txt
  ├── README.md
  ├── movie_booking/
  │   ├── __init__.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── api/
      ├── __init__.py
      ├── models.py
      ├── serializers.py
      ├── views.py
      ├── urls.py
      └── admin.py
```

## Development Notes

### AI-Assisted Development

This project was developed with assistance from AI tools. The following components were created or significantly influenced by AI-generated code:

- **URL Routing Configuration** (`urls.py`): Router setup and endpoint configuration
- **API ViewSet Structure** (`views.py`): Initial viewset implementations
- **Serializers** (`serializers.py`): Base serializer classes
- **Documentation**: This README file structure and content

All AI-generated code has been reviewed, tested, and customized to fit the specific requirements of this project. While AI provided the foundation and boilerplate, the business logic and final implementation decisions were made by human developers.

---

**Note**: This is a learning/demonstration project. For production use, additional security measures, testing, and optimization would be required.
