
# **Let's Chat! - Real-time Chat Application**

LetsChat is a real-time chat application built using **Django** on the backend and **React** on the frontend. The app features user authentication with **JWT tokens** and real-time messaging via **WebSocket connections** using **Django Channels**. It allows users to sign up, log in, and send real-time messages in a chat room while securely authenticated. Each user has their own unique color in the chat.

## **Features**
- **User Authentication**: Secure user signup and login using JWT tokens.
- **WebSocket-based Messaging**: Real-time messaging through WebSockets with Django Channels.
- **Real-time Communication**: Users can send and receive messages instantly.
- **User-Specific Colors**: Each user gets their own color in the chat interface.
- **Token-based WebSocket Authentication**: Only authenticated users can connect to WebSockets.

## **Tech Stack**
- **Backend**: Django, Django Rest Framework, Django Channels
- **Frontend**: React, React Router, WebSockets, Axios
- **Database**: SQLite (default) or any other Django-supported database
- **Authentication**: JWT (JSON Web Tokens)

## **Getting Started**

### **Prerequisites**

Make sure you have the following installed:
- **Python 3.x**
- **Node.js** and **npm**
- **Git**

### **Backend Setup (Django)**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/esNIMA/LetsChat.git
   cd LetsChat/backend
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate     # For macOS/Linux
   .\venv\Scripts\activate      # For Windows
   ```

3. **Install the Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:
   Create an admin user for accessing the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Backend Server**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

### **Frontend Setup (React)**

1. **Navigate to the frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install Dependencies**:
   Install the necessary npm packages for the React frontend:
   ```bash
   npm install
   ```

3. **Run the Frontend**:
   ```bash
   npm run dev
   ```

4. **Access the Application**:
   Open a browser and go to:
   - **Backend (Django):** `http://localhost:8000`
   - **Frontend (React):** `http://localhost:5173`

### **Configuration**

- **CORS**: If you're developing locally, ensure that CORS is properly configured in `settings.py`:
  ```python
  CORS_ALLOWED_ORIGINS = [
      'http://localhost:5173',  # React frontend
  ]
  ```

- **JWT Settings**: You can configure JWT settings in `settings.py`:
  ```python
  SIMPLE_JWT = {
      'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
      'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
      'ROTATE_REFRESH_TOKENS': False,
      'BLACKLIST_AFTER_ROTATION': True,
      'AUTH_HEADER_TYPES': ('Bearer',),
  }
  ```

---

## **Usage**

### **1. User Signup and Login**

- **Signup**: New users can sign up through the frontend interface.
- **Login**: Existing users can log in, which will generate a JWT token used for authenticating WebSocket connections.

### **2. Chat Room**

Once logged in, users can access the chat room where they can send and receive messages in real-time. Each user is assigned a unique color for their messages, and the WebSocket ensures messages are delivered instantly without reloading the page.

---

## **API Endpoints**

| Method | Endpoint           | Description                          |
|--------|--------------------|--------------------------------------|
| POST   | `/users/signup/`    | Register a new user                  |
| POST   | `/users/login/`     | Log in an existing user              |
| GET    | `/ws/chat/`         | WebSocket endpoint for real-time chat|

---

## **WebSocket Authentication**

The WebSocket connection is protected using JWT tokens. When a user connects to the WebSocket, the token is passed in the query string and is verified on the server before allowing access to the chat room.

### **Frontend Example:**
```javascript
const token = localStorage.getItem('access_token');
const ws = new WebSocket(`ws://localhost:8000/ws/chat/?token=${token}`);

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log(data.message);
};
```

---

## **Running Tests**

To run tests on the Django backend:

```bash
python manage.py test
```

To run tests on the React frontend (if applicable):

```bash
npm run test
```

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push the changes:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request on GitHub.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any questions or issues, please contact me through my GitHub profile: [esNIMA](https://github.com/esNIMA).

