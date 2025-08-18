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
| `/api/auth/register`   | POST   | Register a new user          | `{ "username": "kapil", "password": "12345" }` | `{ "message": "User registered successfully" }` |
| `/api/auth/login`      | POST   | Login with credentials       | `{ "username": "kapil", "password": "12345" }` | `{ "token": "jwt-token-here" }` |
| `/api/files/upload`    | POST   | Upload a file                | multipart/form-data | `{ "file_id": 1, "status": "Uploaded" }` |
| `/api/files/:id`       | GET    | Get file details by ID       | `/api/files/1` | `{ "file_id": 1, "name": "report.pdf", "status": "Delivered" }` |
| `/api/files/:id/track` | GET    | Track who viewed the file    | `/api/files/1/track` | `[{"user": "John", "time_spent": "5 mins"}]` |

---

✅ You can also add:
- **Authentication requirement** (Yes/No)  
- **Status codes** (`200, 400, 401, 404`)  
- **Headers** if needed  

For example, if you want a simpler test table:

```markdown
| Test Case | Endpoint           | Method | Expected Result               |
|-----------|--------------------|--------|--------------------------------|
| 1         | `accounts/auth/logout/`  | POST   | It logouts from the system      |
| 2         | `accounts/auth/login/`| POST   | Should login the user with email and possword |
| 3         |  `accounts/auth/register/`    | POST  | Should register the user with username email and passowrd  |
| 3         |  `accounts/auth/me/`    | GET  | Should return the information about the account    |
