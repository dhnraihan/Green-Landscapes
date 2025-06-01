# Green Landscapes - Professional Landscaping Service Website

A comprehensive website for a landscaping service business built with Django. This website allows customers to view services, browse a portfolio of completed projects, book appointments, and manage their accounts.

![Restaurant Management System](demo.webp)

## ✨ Features

### For Customers
- **Responsive Design**: Mobile-friendly interface built with Tailwind CSS
- **Service Catalog**: Browse and search available landscaping services
- **Project Gallery**: View before/after images of completed projects
- **Online Booking**: Real-time availability and appointment scheduling
- **User Dashboard**: Manage bookings, view history, and update profile
- **Service Areas**: Check if we service your location

### For Administrators
- **Admin Dashboard**: Comprehensive management interface
- **Booking Management**: View, confirm, and manage appointments
- **Portfolio Management**: Showcase completed projects
- **User Management**: Handle customer accounts and permissions
- **Service Management**: Add, update, or remove services

## 🛠 Technical Stack

- **Backend**: 
  - Django 5.2
  - Django Allauth (for authentication)
  - Django Crispy Forms (for form rendering)

- **Frontend**:
  - HTML5, CSS3, JavaScript (ES6+)
  - Tailwind CSS 3.0+ for styling
  - Alpine.js for interactive components
  - Responsive design for all devices

- **Database**:
  - SQLite (development)
  - PostgreSQL (production-ready)

- **Deployment**:
  - Gunicorn / uWSGI
  - Nginx (recommended)
  - Docker support included

- **Other Features**:
  - CSRF protection
  - XSS protection
  - Secure password hashing
  - Session management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Node.js and npm (for frontend assets)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhnraihan/Green-Landscapes.git
   cd Green-Landscapes
   ```

2. **Set up a virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   .\venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Copy the example environment file and update it with your settings:
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file with your configuration.

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Install frontend dependencies**
   ```bash
   npm install
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Website: http://127.0.0.1:8000/
    - Admin: http://127.0.0.1:8000/admin/
    - API Documentation: http://127.0.0.1:8000/api/docs/

### Development Commands

- Run tests:
  ```bash
  python manage.py test
  ```

- Run with custom settings:
  ```bash
  python manage.py runserver --settings=landscaping_project.settings.local
  ```

- Create new app:
  ```bash
  python manage.py startapp your_app_name
  ```

## 📁 Project Structure

```
landscaping/
├── accounts/                 # User authentication and profile management
├── bookings/                 # Booking and appointment system
├── core/                     # Core functionality and base templates
├── gallery/                  # Portfolio and project gallery
├── services/                 # Service management
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/                # HTML templates
│   ├── accounts/
│   ├── bookings/
│   ├── core/
│   ├── gallery/
│   └── services/
├── media/                    # User-uploaded files
├── requirements/             # Python requirements files
├── .env.example             # Example environment variables
├── manage.py                # Django management script
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root with the following variables:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=webmaster@example.com
```

### Database
By default, the project uses SQLite. For production, consider using PostgreSQL:

1. Install PostgreSQL
2. Update DATABASE_URL in `.env`:
   ```
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
   ```
3. Install PostgreSQL adapter:
   ```bash
   pip install psycopg2-binary
   ```

## Configuration

The main configuration is in `landscaping_project/settings.py`. Key settings to customize:
- `SECRET_KEY`: Update for production
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Add your domain in production
- Email configuration for sending notifications
- Database settings if switching from SQLite

## 🚀 Future Features

### In Development
- [ ] Online payment integration (Stripe/PayPal)
- [ ] Customer review system
- [ ] Service area mapping
- [ ] Employee scheduling

### Planned
- [ ] Mobile app for customers
- [ ] Interactive 3D garden designer
- [ ] Automated quote generation
- [ ] Integration with weather services
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request


## 📞 Contact

For support or questions, please contact [Raihan] at [hello@raihan.xyz](mailto:hello@raihan.xyz).

---

<div align="center">
  <p>Made with ❤️ by Raihan</p>
  <p>© 2025 Green Landscapes. All rights reserved.</p>
</div>
