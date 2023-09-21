# DataDrivenSystemUsingDjango

# Data Drive System

**Description:**
This project is a Data Drive System inspired by Google Drive, built using Django. 
It allows users to create, organize, and manage their files and folders, just like in Google Drive. 
The project includes features such as user authentication, folder creation, nested folders, 
and CRUD (Create, Read, Update, Delete) operations on files and folders.

**Key Features:**
- User authentication: Users can create accounts and log in.
- Folder Hierarchy: Users can create nested folders of any depth.
- CRUD Operations: Users can perform Create, Read, Update, and Delete operations on files and folders.

**Technologies Used:**
- Django (version 3+)
- Django ORM (Object-Relational Mapping)
- Middleware
- Raw SQL Queries (specifically SELECT queries)
- HTML and CSS (for the user interface)

**Project Structure:**
- `datadrivesystem/`: The main Django project folder.
- `drive/`: The Django app folder for the Data Drive System.
- `drive/views.py`: Contains the views for the project, including user profile and CRUD operations on folders and files.
- `drive/templates/`: HTML templates for rendering views.
- `drive/models.py`: Defines the database models, including User, Folder, and File.
- `drive/urls.py`: Defines URL patterns and routes.
- `drive/forms.py`: Contains forms for user registration and folder/file creation.

**Usage:**
1. Clone the project to your local machine using Git.
2. Set up a virtual environment and install project dependencies.
3. Configure your database settings in `datadrivesystem/settings.py`.
4. Apply migrations and create database tables using `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.
6. Access the project in your web browser at `http://localhost:8000/`.

**Authors:**
- Tejaswini Jena
