# Employee Management System

## Overview

Employee Management System is a web-based application developed using Python, Django, and PostgreSQL. The system helps organizations manage employee records efficiently through a user-friendly interface and REST APIs.

The application provides employee information management, department management, authentication, database integration, and CRUD operations.

---

## Features

* Employee Management (Create, Read, Update, Delete)
* Department Management
* User Authentication
* Django ORM Integration
* PostgreSQL Database Connectivity
* REST API Development using Django REST Framework
* Admin Dashboard
* Form Validation and Error Handling
* Responsive User Interface

---

## Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL

### Frontend

* HTML
* CSS
* JavaScript

### Tools

* Git
* GitHub
* VS Code
* Postman

---

## Project Structure

employee_management_system/

├── manage.py

├── employee_management/

│ ├── settings.py

│ ├── urls.py

│ └── ...

├── employees/

│ ├── models.py

│ ├── views.py

│ ├── api_views.py

│ ├── serializers.py

│ ├── forms.py

│ ├── middleware.py

│ ├── admin.py

│ └── urls.py

├── templates/

│ ├── base.html

│ ├── employee_list.html

│ └── employee_form.html

└── requirements.txt

---

## Database Schema

### Department

| Field | Type      |
| ----- | --------- |
| id    | Integer   |
| name  | CharField |

### Employee

| Field        | Type         |
| ------------ | ------------ |
| id           | Integer      |
| name         | CharField    |
| email        | EmailField   |
| phone        | CharField    |
| designation  | CharField    |
| salary       | DecimalField |
| department   | ForeignKey   |
| joining_date | DateField    |

---

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Update database credentials in:

```python
employee_management/settings.py
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## API Endpoints

### Employee APIs

```http
GET /api/employees/
```

```http
POST /api/employees/
```

```http
PUT /api/employees/{id}/
```

```http
DELETE /api/employees/{id}/
```

---

## Learning Outcomes

* Django Project Structure
* Django ORM
* PostgreSQL Integration
* CRUD Operations
* REST API Development
* Middleware Implementation
* Authentication & Authorization
* Git Version Control

---

## Author

Deepak Kumar

GitHub: https://github.com/Deepakkumar2429

LinkedIn: https://linkedin.com/in/deepak29kumar
