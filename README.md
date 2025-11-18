# TASK4-PYTHON
# Flask User Management API

This project is a simple **User Management API** built using **Flask**.\
It supports CRUD operations such as creating, reading, updating, and
deleting users.

------------------------------------------------------------------------

## 🚀 Features

-   Get all users\
-   Get a user by ID\
-   Add a new user\
-   Update an existing user\
-   Delete a user

------------------------------------------------------------------------

## 📁 Project Structure

    app.py        # Main Flask application
    README.md     # Project documentation

------------------------------------------------------------------------

## 🛠 Requirements

Install dependencies:

    pip install flask

------------------------------------------------------------------------

## ▶️ How to Run

    python app.py

The API will run at:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📌 API Endpoints

### **1. Home**

**GET** `/`\
Returns a message confirming the API is running.

------------------------------------------------------------------------

### **2. Get all users**

**GET** `/users`

------------------------------------------------------------------------

### **3. Get user by ID**

**GET** `/users/<int:user_id>`

------------------------------------------------------------------------

### **4. Add a new user**

**POST** `/users`

Send JSON:

``` json
{
  "id": 3,
  "name": "New User",
  "email": "new@example.com"
}
```

------------------------------------------------------------------------

### **5. Update user**

**PUT** `/users/<int:user_id>`

------------------------------------------------------------------------

### **6. Delete user**

**DELETE** `/users/<int:user_id>`

------------------------------------------------------------------------

## 📞 Contact

For any issues, feel free to ask!
