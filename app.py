# app.py

from flask import Flask, render_template, request, jsonify
from models import create_table, insert_user, get_users, update_user, delete_user, clear_database

app = Flask(__name__)

# clear_database()
create_table()

@app.route('/')
def home():
    insert_user('John Doe', 'johndoe@example.com', 30)
    users = get_users()
    return render_template('index.html', users=users)

@app.route('/update', methods=['POST'])
def update():
    user_id = request.form['user_id']
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    update_user(user_id, name, email, age)
    return 'User updated'


@app.route('/delete_user', methods=['POST'])
def delete_user_route():
    user_id = request.form['user_id']
    delete_user(user_id)
    return jsonify({'message': 'User deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)



