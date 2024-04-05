import os
import json
# Load the JSON file
with open("password-manager-2bed3-firebase-adminsdk-ghgx0-3a780548e5.json") as f:
    data = json.load(f)

# Set environment variables
os.environ["SERVICE_ACCOUNT_KEY_PATH"] = 'password-manager-2bed3-firebase-adminsdk-ghgx0-3a780548e5.json'
os.environ["TYPE"] = data["type"]
os.environ["PROJECT_ID"] = data["project_id"]
os.environ["PRIVATE_KEY_ID"] = data["private_key_id"]
os.environ["PRIVATE_KEY"] = data["private_key"]
os.environ["CLIENT_EMAIL"] = data["client_email"]
os.environ["CLIENT_ID"] = data["client_id"]
os.environ["AUTH_URI"] = data["auth_uri"]
