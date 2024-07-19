readme
# User Authentication Service

## Overview

This project implements a comprehensive user authentication service using Flask, providing essential features for user registration, login, session management, and password reset functionalities. The service ensures secure handling of user data with hashed passwords and UUID-based session IDs.

## Features

- **User Registration:** Securely register new users with unique email addresses and hashed passwords.
- **User Login:** Authenticate users using email and password, generating session IDs for maintaining logged-in states.
- **Session Management:** Create and destroy user sessions, ensuring secure access to user profiles.
- **Password Reset:** Generate and validate password reset tokens, allowing users to securely update their passwords.

## Problem Solved

This service addresses the critical need for secure and efficient user authentication in web applications, providing a robust foundation for managing user sessions and sensitive data. By implementing industry-standard security practices, it enhances the overall safety and usability of web-based systems, making it a valuable addition to any software development project.

## How to Use

1. **Register a New User:** POST `/users` with `email` and `password`.
2. **Login a User:** POST `/sessions` with `email` and `password`.
3. **Access Profile:** GET `/profile` with a valid session ID.
4. **Reset Password:** POST `/reset_password` with `email`, and PUT `/reset_password` with `email`, `reset_token`, and `new_password`.

This project exemplifies best practices in user authentication, ensuring both security and user-friendliness.
