# StudyBud: Django Chat Application
StudyBud is a web-based platform built with Django and Django REST Framework where users can create chat rooms, exchange real-time messages, and manage their profiles.

## Features
- User Authentication: Register, log in, and log out functionalities using Django's authentication system.
- Chat Rooms: Create new chat rooms with topics and descriptions.
- Messaging: Real-time messaging within chat rooms, displaying user information and timestamps.
- Profile Management: View and update user profiles, including username and email.

## Technology Stack
- Backend: Django (Python)
- REST API: Django REST Framework
- Frontend: HTML, CSS
- Database: SQLite

## mInstallation
1)Clone the repository:
   git clone https://github.com/your-username/studybud.git
   cd studybud
2)Install the required dependencies:
   pip install -r requirements.txt
3)Apply database migrations:
   python manage.py migrate
4)Create a superuser to access the admin interface:
   python manage.py createsuperuser
5)Run the development server:
   python manage.py runserver
6)Open your web browser and navigate to http://localhost:8000

## Usage
-Registration and Login: Visit /register to create a new user account. Access /login to log in using your credentials.
-Creating and Joining Chat Rooms: Create a new chat room by visiting /create-room. View available chat rooms on the homepage (/) and click to join.
-Sending Messages: Post messages in chat rooms and view real-time updates.

## Project Structure
-views.py: Contains the main logic for handling requests and responses.
-urls.py: Defines the URL routes for the application.
-models.py: Defines the database models.
-forms.py: Contains form definitions for user registration and chat room creation.
-templates/: Directory containing HTML templates for the web interface.
-static/: Directory for static files like CSS and images.

## API Endpoints
- GET /api/rooms/: Retrieve all chat rooms.
- POST /api/create-room/: Create a new chat room.
- GET /api/room/<id>/: Retrieve details of a specific chat room.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

