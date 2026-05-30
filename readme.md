# Added Extension: Categories REST API
This Flask application has been enhanced with a backend REST API that handles Categories using full CRUD functionality and JSON messaging.

## API Endpoints:
- `POST /api/categories` - Create a category (Requires json: `{"name": "xyz"}`)
- `GET /api/categories` - Fetch all categories
- `PUT /api/categories/<id>` - Update category name/description
- `DELETE /api/categories/<id>` - Delete a category
- 
# Flask Blog Web App

This is a simple blog web application built with Flask, a micro web framework written in Python. It uses SQLite3 as the database and Flask-SQLAlchemy for Object Relational Mapping (ORM).

## Features

- Create, read, update, and delete (CRUD) operations for blog posts.
- SQLite3 database for storing blog post data.
- Flask-SQLAlchemy for easy database management.

## Technologies Used

- Flask: A micro web framework for Python.
- SQLite3: A C library that provides a lightweight disk-based database.
- Flask-SQLAlchemy: An extension for Flask that simplifies the use of SQLAlchemy with Flask by providing useful defaults and extra helpers.
- Bootstrap Library for responsive design.
- HTML5/CSS3 for page layouts.

## Python Libraries Used

- flask
- flask_sqlalchemy
- datetime

## Routes

- `'/'`: The home page where all blog posts are displayed.
- `'/new_post'`: The page where a new blog post can be created.
- `'/edit/<int:id>'`: The page where an existing blog post can be edited.
- `'/delete/<int:id>'`: The route that handles the deletion of a blog post.

## Setup and Installation

1. Clone the repository.
2. Install the required Python libraries with `pip install -r requirements.txt`.
3. Run the application with `python app.py`.

## Usage

Visit `'/'` to see all blog posts. Click on "Create Post" to create a new blog post. Click on "Edit" to edit an existing blog post. Click on "Delete" to delete a blog post.

## Future Improvements

- User authentication for secure blog post management.
- Commenting functionality for blog posts.
- Improved UI/UX design.

## Live URL 
- Link: https://blog-webapp-using-flask-and-sqlite3-1.onrender.com/