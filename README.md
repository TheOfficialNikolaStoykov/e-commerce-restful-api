# E-commerce RESTful API
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Stripe](https://img.shields.io/badge/Stripe-5469d4?style=for-the-badge&logo=stripe&logoColor=ffffff) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

This project provides a comprehensive E-commerce backend API built with Django REST framework. The API includes core functionalities for managing users, products, orders, carts, and shipping. It also supports user authentication, product reviews, and integrations with third-party services like Stripe and Shippo for payments and shipping.

## Features

- **User Management**: User registration, login, logout, profile management.
- **Product Management**: Add, update, delete, and view products and categories.
- **Order Management**: Place orders, view order history, manage order status.
- **Cart Management**: Add, edit, delete items from the cart.
- **Payment Integration**: Stripe integration for processing payments.
- **Shipping Integration**: Shippo integration for calculating shipping rates and managing deliveries.
- **Admin Access**: Admin-only features for managing products, categories, and order statuses.

## Setup Instructions

### Prerequisites

- Python 3.11 or higher
- Django 4.x or higher
- Virtual environment setup (venv)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/TheOfficialNikolaStoykov/e-commerce-restful-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd e-commerce-restful-api
    ```

3. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser for accessing the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

8. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

### API Documentation

API documentation is available via Swagger UI. You can access it [here](https://theofficialnikolastoykov.github.io/e-commerce-restful-api/).

For example:

```
http://127.0.0.1:8000/swagger/
```

### Running Tests

To run tests, use the following command:

```bash
python manage.py test
```

To run coverage, use the following commands sequentially:
```bash
coverage run manage.py test
```
```bash
coverage report
```

## Technologies Used

- **Backend Framework**: Django REST Framework
- **Payment Integration**: Stripe API
- **Shipping Integration**: Shippo API
- **Authentication**: Django Token Authentication
- **Database**: SQLite
- **API Documentation**: Swagger UI

## License

This project is licensed under the MIT License - see the LICENSE file for details.
