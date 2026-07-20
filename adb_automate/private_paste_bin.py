import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
# Access the environment variables
api_key = os.getenv("API_DEV_KEY")
user_name = os.getenv("USER_NAME")
user_passwd = os.getenv("USER_PASSWD")


def get_logined():
    login_params = {
        "api_dev_key": api_key,
        "api_user_name": user_name,
        "api_user_password": user_passwd,
    }
    login_response = requests.post(
        "https://pastebin.com/api/api_login.php", data=login_params
    )
    print("login response is : , login_response", login_response)
    return login_response


def upload_to_private_pastebin(user_api_key):
    # Get clipboard content
    clipboard_content = "sample paste content"

    # Prepare your parameters for the API request
    params = {
        "api_dev_key": api_key,
        "api_user_key": user_api_key,
        "api_option": "paste",
        "api_paste_code": clipboard_content,
        "api_paste_name": "Private Clipboard Paste",
        "api_paste_private": "1",
        "api_paste_expire_date": "10M",
    }

    # Make the POST request to Pastebin
    response = requests.post("https://pastebin.com/api/api_post.php", data=params)

    # Check if the request was successful
    if response.status_code == 200:
        print(
            f"Uploaded! You can access your paste at: https://pastebin.com/{response.text}"
        )
    else:
        print("Failed to upload:", response.text)


if __name__ == "__main__":
    user_api_key = get_logined()  # This will be your user API key

    your_user_api_key = user_api_key

    upload_to_private_pastebin(your_user_api_key)
