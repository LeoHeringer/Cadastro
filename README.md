
# User Registration API

This project is a Django-based API for user registration and management. It allows users to register, update their information, and delete their accounts. The API supports both JSON and XML formats for input and output.

## Features

- User registration
- User information update
- User deletion
- JWT Authentication
- CORS enabled

## Endpoints

### User Registration

- `POST /create-user/`
  - JSON: Creates a new user.
  - XML: Creates a new user.

### Get Users

- `GET /get-users-json/`
  - Returns a list of users in JSON format.
- `GET /get-users-xml/`
  - Returns a list of users in XML format.

### Get User by Nickname

- `GET /get-by-nick-json/?user=<username>`
  - Returns user details in JSON format.
- `GET /get-by-nick-xml/?user=<username>`
  - Returns user details in XML format.

### Update User

- `PUT /update-user-json/?id-usuario=<user_id>`
  - Updates user information in JSON format.
- `PUT /update-user-xml/?id-usuario=<user_id>`
  - Updates user information in XML format.

### Delete User

- `DELETE /delete-user-json/?id-usuario=<user_id>`
  - Deletes a user in JSON format.
- `DELETE /delete-user-xml/?id-usuario=<user_id>`
  - Deletes a user in XML format.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/leoHeringer/user-registration-api.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'registration',
           'USER': 'root',
           'PASSWORD': 'root',
           'HOST': '127.0.0.1',
           'PORT': '3306'
       }
   }
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```

## Usage

Use tools like [Postman](https://www.postman.com/) or `curl` to test the endpoints. Here are some example requests:

### Create User (JSON)
```bash
curl -X POST "http://localhost:8000/create-user/" -H "Content-Type: application/json" -d '{"username": "john", "password": "password123"}'
```

### Get Users (JSON)
```bash
curl -X GET "http://localhost:8000/get-users-json/" -H "Authorization: Bearer <your_token>"
```

### Get User by Nickname (JSON)
```bash
curl -X GET "http://localhost:8000/get-by-nick-json/?user=john" -H "Authorization: Bearer <your_token>"
```

### Update User (JSON)
```bash
curl -X PUT "http://localhost:8000/update-user-json/?id-usuario=1" -H "Content-Type: application/json" -H "Authorization: Bearer <your_token>" -d '{"is_superuser": true}'
```

### Delete User (JSON)
```bash
curl -X DELETE "http://localhost:8000/delete-user-json/?id-usuario=1" -H "Authorization: Bearer <your_token>"
```

## Contributing

Feel free to submit issues and pull requests.
