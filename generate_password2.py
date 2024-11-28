import bcrypt

new_password = "Jumio1512"  # Replace with your desired password
hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
print(hashed_password.decode())
