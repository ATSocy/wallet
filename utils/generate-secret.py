import hashlib
import secrets

# Generate a secure random number as the base for the key
random_number = secrets.token_bytes(32)  # 32 bytes = 256 bits

# Use SHA256 to hash the secure random number
sha256_key = hashlib.sha256(random_number).hexdigest()

print(sha256_key)