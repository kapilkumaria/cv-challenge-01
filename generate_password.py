import bcrypt

# Define your new password
new_password = "matarani123"  # Replace with your desired password

# Generate the hashed password
hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
print(f"Hashed Password: {hashed.decode()}")

# To verify a password (optional):
#stored_hash = b"$2b$12$4.Xl09No2.YRebK0A7f3X.1NSqFozXL3OTdLWwpgcK/8vkJZmf2"  # Replace with the existing hash
#if bcrypt.checkpw(new_password.encode(), stored_hash):
#    print("Password matches the stored hash!")
#else:
#    print("Password does not match.")

