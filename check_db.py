from app import app, db, User  # Import your app and User model

with app.app_context():
    # Fetch all users from the database
    users = User.query.all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Password Hash: {user.password_hash}")