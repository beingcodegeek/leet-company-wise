import secrets

# Generate a secure random key
secret_key = secrets.token_hex(16)  # 16 bytes will give you a 32-character hex string
print(secret_key)
