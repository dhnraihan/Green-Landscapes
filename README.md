# Green Landscapes - Professional Landscaping Service Website

A comprehensive website for a landscaping service business built with Django. This website allows customers to view services, browse a portfolio of completed projects, book appointments, and manage their accounts.

## Features

- **Home Page**: Welcoming landing page with featured services, testimonials, and call-to-action buttons
- **Services**: Browse available landscaping services with detailed descriptions
- **Gallery**: View portfolio of completed projects with before/after comparisons
- **Booking System**: Schedule landscaping services with date and time selection
- **User Accounts**: Register, login, and manage profile and bookings
- **Admin Dashboard**: Manage services, bookings, and user accounts through Django admin
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

## Technical Stack

- **Backend**: Django 5.2
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL
- **Authentication**: Django built-in auth system
- **Form Processing**: Django Crispy Forms

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dhnraihan/Green-Landscapes.git
cd Green-Landscapes
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the website at http://127.0.0.1:8000/ and admin at http://127.0.0.1:8000/admin/

## Project Structure

- `core/`: Core app with homepage, contact, and base functionality
- `services/`: Services app for managing and displaying landscaping services
- `gallery/`: Gallery app for portfolio and before/after images
- `bookings/`: Booking system for scheduling services
- `accounts/`: User account management
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)
- `media/`: User-uploaded content

## Configuration

The main configuration is in `landscaping_project/settings.py`. Key settings to customize:
- `SECRET_KEY`: Update for production
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Add your domain in production
- Email configuration for sending notifications
- Database settings if switching from SQLite

## Future Features

- Online Payment Integration
- Blog Section
- Email Reminders/Notifications
- Monthly Service Subscription System
- Multi-language Support
