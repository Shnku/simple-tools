import requests


def upload_to_private_pastebin(api_dev_key, user_api_key):
    # Get clipboard content
    clipboard_content = "sample paste content"

    # Prepare your parameters for the API request
    params = {
        "api_dev_key": api_dev_key,
        "api_user_key": user_api_key,
        "api_option": "paste",
        "api_paste_code": clipboard_content,
        "api_paste_name": "Private Clipboard Paste",
        "api_paste_private": "1",  # Make the paste private
        "api_paste_expire_date": "10M",  # Expires in 10 minutes
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
    login_response = requests.post(
        "https://pastebin.com/api/api_login.php", data=login_params
    )
    print("login response is : , login_response", login_response)
    user_api_key = login_response.text  # This will be your user API key

    your_user_api_key = user_api_key

    upload_to_private_pastebin(your_api_dev_key, your_user_api_key)
