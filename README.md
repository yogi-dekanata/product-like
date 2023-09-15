Certainly! Here's the translated `README.md` file content:

---

# FavShop Web Application

FavShop is a web application that allows users to like products and view a list of liked products.

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the App](#running-the-app)
- [API Documentation](#api-documentation)
- [Testing](#testing)

## Installation

1. Clone this repository to your local machine.
    ```sh
    git clone https://github.com/yogi-dekanata/product-like.git
    ```


2. Build the Docker containers.
    ```sh
    docker-compose build
    ```

## Database Setup

1. Migrate the database to initialize the schema and tables.
    ```sh
    docker-compose run web python manage.py migrate
    ```

## Running the App

1. Run the application.
    ```sh
    docker-compose up
    ```
    Access the application at `http://localhost:8000`.

## API Documentation

API documentation can be accessed via Swagger at the URL `http://localhost:8000/swagger/`.
