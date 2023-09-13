# Project Name

A brief description of your Django project.

## Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python: This project is built using Python. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/your-username/your-project.git

     Navigate to the project directory:

        ```cd Crud-API/```

    Create a virtual environment (recommended) to isolate project dependencies:
        ```python -m venv venv```

    Activate the virtual environment:
    ```On Windows:

            bash
            venv\Scripts\activate```
   ```On macOS and Linux:
        bash
        source venv/bin/activate
        Install project dependencies using pip:

        bash
        pip install -r requirements.txt```
    
### Usage
# Configure Django settings:

2.  **Create a .env file in the project root directory and add your Django settings. Here's a minimal example:**

        1. env
            DEBUG=True
            SECRET_KEY=your-secret-key
            DATABASE_URL=your-database-url
            Migrate the database:

        2. python manage.py migrate
        Create a superuser (admin) account:

        3. `python manage.py createsuperuser
        Run the development server:`

        python manage.py runserver


Access the Django admin panel at http://localhost:8000/admin/ and log in with the superuser account you created in step 3.

Customize the Django app as per your project requirements by modifying the views, models, serializers, and URLs.

For API endpoints, refer to the API documentation or the URLs defined in your urls.py.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the project on GitHub.

Clone the forked repository to your local machine.

Create a new branch for your feature or bug fix.

Make your changes and commit them with clear, concise commit messages.

Push your changes to your fork on GitHub.

Submit a pull request to the main repository.


## Creating and Reading a Person
* Create a New Person
        To create a new Person object in your Django project, you can use the CreatePersonView endpoint by sending an HTTP POST request with the required data for the new person.

        Endpoint: /api

        Method: POST

        Description: Create a new Person object.

        Request Payload: Provide the data for the new Person object in the request body in JSON format.

        Example Request:

        http
        POST /api
        Content-Type: application/json

        {
        "name": "Alice",
        "name": "Johnson",
        "email": "alice@example.com"
        }
* Response:

If the creation is successful, you will receive a JSON response with a status code of 201 (Created) and the newly created Person object, including its ID.
json
Copy code
{
  "id": 2,
  "name": "Alice",
}

## Read a Person
T```o retrieve information about a specific Person object, you can use the RetrievePersonView endpoint by sending an HTTP GET request with the `person's ID.

Endpoint: /api/<int:pk>

Method: GET

Description: Retrieve details of a Person object by specifying its ID.

Example Request:

http
GET /api/2
Response:

```If the requested person exists, you will receive a JSON response with a status code of 200 (OK) and the details of the Person object.``
json
Copy code
{
  "id": 2,
  "name": "Alice",
}
```If the provided ID does not exist, you will receive a JSON response with a status code of 404 (Not Found) and an error message.```
json
{
  "detail": "Not found."
}


## Using the Endpoint

### Update and Delete a Person by ID

To update and delete a `Person` object in your Django project, you can use the `UpdatePersonView` endpoint by sending HTTP requests with the person's ID. This view supports both updating and deleting operations.

#### Update a Person

- **Endpoint**: `/api/<int:pk>`
- **Method**: PUT/PATCH
- **Description**: Update the details of a `Person` object by specifying its ID.
- **Request Payload**: Provide the updated data for the `Person` object in the request body in JSON format.
- **Example Request**:

 Response:

```If the update is successful, you will receive a JSON response with a status code of 200 (OK) and the updated Person object.```
json
{
  "id": 1,
  "name": "John","
}
```If the provided ID does not exist, you will receive a JSON response with a status code of 404 (Not Found) and an error message.```
json
{
  "detail": "Not found."
}
## Delete a Person
# Endpoint: /api/<int:pk>

Method: DELETE

Description: Delete a Person object by specifying its ID.

Example Request:

http
DELETE /api/1
Response:

```If the deletion is successful, you will receive a JSON response with a status code of 204 (No Content) and a success message.``
json
{
  "message": "Deleted successfully"
}
If the provided ID does not exist, you will receive a JSON response with a status code of 404 (Not Found) and an error message.
json

{
  "detail": "Not found."
}
Make sure to replace /api with the actual URL path you've defined in your Django project's urls.py for the UpdatePersonView.
