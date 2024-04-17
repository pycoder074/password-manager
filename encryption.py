import bcrypt

def encrypt(data):
    data = data.encode('utf-8')  # Encode the string as bytes
    salt = bcrypt.gensalt()
    encrypted = bcrypt.hashpw(data, salt)
    return {
        'salt': salt.decode('utf-8'),  # Decode the salt to UTF-8 string
        'encrypted': encrypted.decode('utf-8')  # Decode the encrypted hash to UTF-8 string
    }

if __name__ == '__main__':
    data = 'Pandek2008'
    encrypted_data = encrypt(data)
    print(encrypted_data)
