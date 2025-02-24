# Sweet Scoop 🍦 - Ice Cream Website

## Overview

Sweet Scoop is a Django-based web application for an ice cream shop. It allows users to browse different ice cream flavors, learn about the company, and contact the company through a form.

## Project Structure

```
Ice Cream/
├── db.sqlite3
├── home/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_contact_date.py
│   │   ├── 0003_rename_message_contact_desc.py
│   │   ├── 0004_alter_contact_desc.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── Ice Cream/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── static/
│   ├── css/
│   │   ├── contact.css
│   │   ├── style.css
│   ├── img/
│   ├── services.css
│   ├── test.txt
├── templates/
│   ├── about.html
│   ├── base.html
│   ├── contact.html
│   ├── index.html
│   ├── services.html
│   ├── signin.html
│   ├── signup.html
```

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git

### Steps

1. **Clone the Repository**: Clone your project repository from GitHub (replace `<repository-url>` with your actual repository URL):
    ```sh
    git clone <repository-url>
    cd Ice Cream
    ```

2. **Create Virtual Environment**: Run the following command to create a virtual environment named `venv`:
    ```sh
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - **On macOS and Linux**:
        ```sh
        source venv/bin/activate
        ```
    - **On Windows**:
        ```sh
        .\venv\Scripts\activate
        ```

4. **Install Dependencies**: With the virtual environment activated, install the dependencies listed in the requirements.txt file:
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply Migrations**: Run the following command to apply database migrations:
    ```sh
    python manage.py migrate
    ```

6. **Create Superuser (Optional)**: If you want to access the Django admin site, create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the Development Server**: With the virtual environment activated, run the Django development server:
    ```sh
    python manage.py runserver
    ```

8. **Access the Project**: Open your web browser and go to `http://127.0.0.1:8000/` to see your Django project running.

## Applications

### Home

- **Models**: Defines the `Contact` model for storing contact form submissions.
- **Views**: Handles rendering of the homepage, about page, services page, contact form, sign-in, and sign-up pages.
- **URLs**: Maps URLs to views.
- **Admin**: Registers the `Contact` model with the Django admin site.

### Ice Cream

- **Settings**: Configuration for the Django project.
- **URLs**: Root URL configuration, includes URLs from the `home` app.
- **WSGI/ASGI**: Configuration for deploying the project.

## Static Files

- **CSS**: Contains stylesheets for different pages.
- **Images**: Placeholder for images used in the project.

## Templates

- **Base Template**: `base.html` - The base template that other templates extend.
- **Page Templates**: Templates for different pages like `index.html`, `about.html`, `contact.html`, `services.html`, `signin.html`, and `signup.html`.

## Models

### Contact

Defined in `home/models.py`:

```python
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField(max_length=500)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
```

## Views

Defined in `home/views.py`:

- `index`: Renders the homepage.
- `about`: Renders the about page.
- `services`: Renders the services page.
- `contact`: Handles contact form submissions and renders the contact page.
- `signin`: Renders the sign-in page.
- `signup`: Renders the sign-up page.

## URLs

Defined in `home/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("signin", views.signin, name='signin'),  
    path("signup", views.signup, name='signup'),
]
```

## Admin

Defined in `home/admin.py`:

```python
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
```

## Settings

Defined in `Ice Cream/settings.py`:

- **Database**: Configured to use SQLite.
- **Static Files**: Configured to serve static files from the `static` directory.
- **Templates**: Configured to use the `templates` directory.

## Running Tests

To run tests, use the following command:

```sh
python manage.py test
```

## Deployment

To deploy the project, configure the `Ice Cream/settings.py` file for production and use a WSGI/ASGI server to serve the application.

---

This documentation provides an overview of the project structure, installation steps, and key components. Adjust the content as needed to fit your specific project requirements.

Similar code found with 1 license type
