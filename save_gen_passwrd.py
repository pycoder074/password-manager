import firebase_admin
from firebase_admin import firestore, credentials
import getpass
from encryption import encrypt
import os
def save_gen_passwrd(passwrd, website = None, username = None):
    cred = os.environ.get("SERVICE_ACCOUNT_KEY_PATH")
    cred = credentials.Certificate(cred)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection('generated_passwords').document()
    doc_ref.set(
        {
        "website" : website,
        "username" : username,
        "passwrd" : passwrd
    }
    )
    print('Generated password saved')
    
if __name__ == '__main__':
    website = input('Website: ')
    username = input('Username: ')
    password = encrypt(getpass.getpass())
    print(website, username, password)
    save_gen_passwrd(password, website, username)