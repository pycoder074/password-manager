import pyotp

# Function to generate a secret key for a user
def generate_secret_key():
    return pyotp.random_base32()

# Function to generate a QR code for a user to scan with their authenticator app
def generate_qr_code(username, secret_key):
    return pyotp.totp.TOTP(secret_key).provisioning_uri(username, issuer_name="YourApp")

# Function to verify the OTP entered by the user
def verify_otp(secret_key, otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(otp)

# Example usage:
# 1. User registration
username = "elliott.kelly08@outlook.com"
secret_key = generate_secret_key()
qr_code = generate_qr_code(username, secret_key)
print("Scan the following QR code with your authenticator app:")
print(qr_code)
# Store the secret_key securely in your database associated with the user account

# 2. User login
entered_otp = input("Enter the OTP from your authenticator app: ")
if verify_otp(secret_key, entered_otp):
    print("OTP verified. Login successful.")
else:
    print("Invalid OTP. Login failed.")
