# Class Enrollment Web Application

This is a web application built with Django for managing class enrollment. It allows students to view and enroll in open classes, as well as view their enrolled classes. Admin users can manage classes and monitor student enrollments.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Name](#name)
- [Video](#vidoe)

## Features

- **Student Features:**
  - View open classes
  - Enroll in open classes
  - View enrolled classes
  - Unenroll from classes

- **Admin Features:**
  - Manage classes (create, edit, delete)
  - Monitor student enrollments
  - Admin authentication and user management

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/class-enrollment-app.git

2.Navigate to the project directory:
  ```bash
  cd class-enrollment-app
  ```

3.Create a virtual environment (optional but recommended):
  ```bash
  python -m venv .venv
  ```

4.Activate the virtual environment:
  ```bash
  Source .venv/Scripts/activate
  ```

5.Install project dependencies:
  ```bash
  pip install -r requirements.txt
  ```

6.Run database migrations:
  ```bash
  python manage.py migrate
  ```

##Usage
1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Access the application in your web browser at http://localhost:8000.
3. You can log in as an admin user to manage classes and view student enrollments. Use the Django admin interface at http://localhost:8000/admin/.

##Name

ธนบูรณ์ จิวริยเวชช์ 6410615055
นวภูมิ นาชัย 6410615071

#Video

https://youtu.be/I9uD2jpEytA
