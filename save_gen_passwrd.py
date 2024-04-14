import firebase_admin
from firebase_admin import firestore, credentials
import os
import json
import getpass
from encryption import encrypt  # Make sure to import encrypt from your encryption module

def save_gen_passwrd(passwrd, website=None, username=None):
    cred_json = os.environ.get("SERVICE_ACCOUNT_KEY")
    cred_dict = json.loads(cred_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection('generated_passwords').document()
    doc_ref.set({
        "website": website,
        "username": username,
        "passwrd": passwrd
    })
    print('Generated password saved')

if __name__ == '__main__':
    website = input('Website: ')
    username = input('Username: ')
    password = encrypt(getpass.getpass())
    print(website, username, password)
    save_gen_passwrd(password, website, username)
