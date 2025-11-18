from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
users = [
    {"id": 1, "name": "John", "email": "john@example.com"},
    {"id": 2, "name": "Divya", "email": "divya@example.com"}
]

# Home route
@app.route('/')
def home():
    return jsonify({"message": "User Management API using Flask is running!"})

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - Create new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify({"message": "User added successfully!", "user": new_user}), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user.update(data)
            return jsonify({"message": "User updated!", "user": user})
    return jsonify({"error": "User not found"}), 404

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted!"})
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)