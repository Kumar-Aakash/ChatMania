# ChatMania

## Description
ChatMania is a real-time chat application allowing users to create rooms, join existing rooms, and communicate with other users in the same room. It is built using [Django](https://www.djangoproject.com/) for the backend, and it utilizes JavaScript for dynamic front-end functionalities.

## Features
- User Authentication: Register and log in to access the chat rooms.
- Room Creation: Create new chat rooms.
- Join Rooms: Join existing chat rooms and participate in discussions.
- Real-time Messaging: Send and receive messages in real-time within a room.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Kumar-Aakash/ChatMania.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ChatMania
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Django migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the Django development server:
   ```sh
   python manage.py runserver
   ```
6. Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Usage
1. Register a new user or log in with existing credentials.
2. Create a new room or join an existing one.
3. Start chatting with other users in the room.


## License
This project is licensed under the [MIT License](LICENSE).

