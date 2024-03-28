import pyotp
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
def generate_qr():
    # Generate a random secret key
    secret_key = pyotp.random_base32()

    # Create a TOTP object
    totp = pyotp.TOTP(secret_key)

    # Generate the QR code URL for the secret key
    qr_code_url = totp.provisioning_uri(name='YourAppName', issuer_name='YourCompany')

    print("Scan this QR code with an authenticator app like Google Authenticator:")
    print(qr_code_url)

    # Generate QR code image
    qr_code = pyqrcode.create(qr_code_url)

    # Save QR code image to file
    qr_code.png('qr_code.png', scale=10)

    # Load the QR code image
    qr_code_image = Image.open('qr_code.png')

    # Decode the QR code image
    decoded_objects = decode(qr_code_image)

    # Print the decoded data
    for obj in decoded_objects:
        print(obj.data.decode('utf-8'))
