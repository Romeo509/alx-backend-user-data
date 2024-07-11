# Basic Authentication Project

## Overview

This project is part of the ALX Full-Stack Engineering program. It focuses on implementing basic authentication mechanisms using Python and Flask. The project covers the essential concepts of user authentication, providing a robust foundation for securing web applications.

## Project Objectives

The main objectives of this project were to:

- Understand the principles of basic authentication.
- Implement authentication mechanisms in a Flask application.
- Handle user credentials securely.
- Ensure the application adheres to best practices in authentication and security.

## Features

- **User Registration:** Allows new users to register by providing an email and password.
- **User Authentication:** Verifies user credentials and grants access to protected resources.
- **Authorization Header Handling:** Extracts and decodes the Base64 authorization header.
- **User Credential Extraction:** Safely extracts user email and password from the decoded header.
- **Authentication Requirement:** Determines if a given endpoint requires authentication.

## Technologies Used

- **Python:** The main programming language used for the project.
- **Flask:** A lightweight WSGI web application framework used for handling HTTP requests.
- **Base64:** Used for encoding and decoding user credentials.
- **Unit Testing:** Implemented to ensure the functionality and reliability of the authentication system.

## Installation and Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/alx-backend-user-data.git
    ```
2. Navigate to the project directory:
    ```sh
    cd alx-backend-user-data/0x01-Basic_authentication
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the application:
    ```sh
    python3 -m api.v1.app
    ```

## Usage

1. Start the Flask application:
    ```sh
    API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
    ```
2. Use `curl` to interact with the API endpoints:
    ```sh
    curl "http://0.0.0.0:5000/api/v1/status"
    ```

## Project Structure

- **api/v1/app.py:** The entry point for the Flask application.
- **api/v1/auth/auth.py:** Contains the base authentication class.
- **api/v1/auth/basic_auth.py:** Implements basic authentication.
- **models/user.py:** Defines the User model for handling user data.
- **tests:** Contains unit tests for the project.

## Conclusion

This project provided a comprehensive understanding of basic authentication and its implementation in a Python-based web application. It reinforced best practices in security and highlighted the importance of handling user credentials securely. The successful completion of this project demonstrates proficiency in web application security and Python programming.

