import bcrypt

# Define your new password
new_password = "password123"  # Replace with your desired password

# Generate the hashed password
hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
print(f"Hashed Password: {hashed.decode()}")

# To verify a password (optional):
stored_hash = b"$2b$12$KoNuGPqRZcWen0q0YDTLCu9Csl0TLsk9H9RYUFFl51hPn6d6kQtCq"  # Replace with the existing hash
if bcrypt.checkpw(new_password.encode(), stored_hash):
    print("Password matches the stored hash!")
else:
    print("Password does not match.")

