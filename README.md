# 📂 File Management & Tracking System currently work in progress

A **File Management & Tracking System** built with Django & Django REST Framework.  

The system keeps a report of:  
- 📍 Where the file is (current location).  
- 👀 Who accessed the file.  
- ⏱️ How much time it stayed at a particular location.  
- 🔄 Complete movement history of the file.  

---

## 🚀 Features
- Upload and manage files securely.  
- Track **file movements** across different locations/departments.  
- Maintain **audit logs**: who accessed the file, when, and for how long.  
- Real-time file **status updates** (like “In Transit”, “At Location A”, “At Location B”).  
- Generate **reports** of file movement history.  
- REST APIs for integration with other applications.  

---

## ⚙️ Tech Stack
- **Python 3.x**  
- **Django**  
- **Django REST Framework (DRF)**  
- **PostgreSQL**

---

## API Endpoints
# API Test Points

Below are the test points for the API:

| Endpoint              | Method | Description                  | Request Example | Response Example |
|------------------------|--------|------------------------------|-----------------|------------------|
| `/api/auth/register`   | POST   | Register a new user          | `{ "username": "kapil","email" : "kapil@gmail.com", "password": "******" }` | `{ "message": "User registered successfully" }` |
| `/api/auth/login`      | POST   | Login with credentials       | `{ "username": "kapil", "password": "12345" }` | `{ "token": "custom token" }` |
| `/api/auth/logout`    | POST   | Helps to logout from the system |`Token in the header section` | `Will logout from the system with no comments` |
|  `/api/auth/me`    | GET    | Will give you the information about the id(account)       | `Token in the header section ` | `{id,email,username}` |

---

✅ You can also add:
- **Authentication requirement** (Yes/No)  
- **Status codes** (`200, 400, 401, 404`)  
- **Headers** if needed  

