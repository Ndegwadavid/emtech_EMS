# Employee Management System

A secure employee management system built with Django and Django REST Framework. Manage employees, track their verification status, and handle administrative tasks efficiently.

## Features

- JWT Authentication for Admin
- Employee Management (CRUD Operations)
- Status Management (Pending/Verified)
- Secure API Endpoints
- Custom Admin Interface
- Activity | Events are being logged in real time and sotred in dir /logs

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd employee_management
```

2. Create virtual environment:
```bash
python -m venv env #if using linux
source env/bin/activate  
# OR
.\env\Scripts\activate  #if using windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- POST `/api/auth/signup/` - Admin registration
- POST `/api/auth/signin/` - Admin login
- POST `/api/auth/token/refresh/` - Refresh JWT token

### Employees
- GET `/api/api/employees/` - List all employees
- POST `/api/api/employees/` - Create new employee
- GET `/api/api/employees/{id}/` - Get employee details
- PUT `/api/employees/{id}/` - Update employee
- DELETE `/api/api/employees/{id}/` - Delete employee
- POST `/api/api/employees/{id}/verify/` - Verify employee

### Documentation
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`
- Admin Interface: `http://127.0.0.1:8000/admin/`

## API Usage Examples

1. Admin Login:
```bash
curl -X POST http://localhost:8000/api/auth/signin/ \
     -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"password"}'
```

2. Create Employee:
```bash
curl -X POST http://localhost:8000/api/employees/ \
     -H "Authorization: Bearer <your_token>" \
     -H "Content-Type: application/json" \
     -d '{
         "full_name": "Ndegwadavid",
         "email": "Ndegwadavid@github.com",
         "phone_number": "0797342380",
         "position": "Developer",
         "department": "IT"
     }'
```

## Security Features

- JWT Authentication
- Input Validation
- Status-based Access Control
- Activity Logging and monitoring
- Rate Limiting <-- to be worked on abit more -->

## Requirements

- In file requirements.txt

## Directory Structure
```
employee_management/
├── accounts/           # Admin authentication
├── employees/          # Employee management
├── static/            # Static files
├── templates/         # HTML templates
└── logs/             # Activity logs
```
