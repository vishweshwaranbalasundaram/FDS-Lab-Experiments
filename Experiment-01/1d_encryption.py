from cryptography.fernet import Fernet

# Generate key and encrypt data
key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(b"Rajalakshmi Engineering College")

# Decrypt data
decrypted_text = f.decrypt(token)

print("Original Data:", b"Rajalakshmi Engineering College")
print("Encrypted Data:", token)
print("Decrypted Data:", decrypted_text)

# Save output
with open("Experiment-01/outputs/1d_output.txt", "w") as file:
    file.write("Original Data: Rajalakshmi Engineering College\n")
    file.write(f"Encrypted Data: {token.decode()}\n")
    file.write(f"Decrypted Data: {decrypted_text.decode()}\n")

print("\nOutput saved successfully!")
