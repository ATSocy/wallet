import bcrypt

password = "redacted".encode()  # Password to hash
salt = bcrypt.gensalt(rounds=11)  # Generate a salt with a cost of 11
hashed_password = bcrypt.hashpw(password, salt)  # Hash the password with the salt

print(hashed_password)
