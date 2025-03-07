# Employ Management System

## Overview
The Employ Management System (EMS) is a web application built using Django that helps manage employee information, tasks, payments, and profiles.

## Features
- User authentication (login, logout, signup)
- Employee profile management
- Task management (pending and submitted tasks)
- Payment management (salary details and transaction history)
- Responsive design with dark mode support

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mE-uMAr/EMS.git
    cd EMS
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```sh
    python manage.py migrate
    ```

4. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage
- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users and other models.
- Use the application to manage employee profiles, tasks, and payments.


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.