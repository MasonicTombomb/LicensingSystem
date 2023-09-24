import requests
from datetime import datetime


def get_licence(licence_key):
    server_url = 'http://10.20.10.112/licences'
    url = f'{server_url}/{licence_key}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result['valid']:
            print(f"Licence is valid. Maximum allowed users: {result['max_users']}")
        else:
            print(f"Licence is invalid for key: {result['licence_key']}")
    elif response.status_code == 403:
        result = response.json()
        if datetime.strptime(result['expiry_date'], "%d/%m/%Y") <= datetime.now():
            print(f"Licence is out of date for key: {licence_key}")
        else:
            print(f"Licence is invalid for key: {licence_key}")
    elif response.status_code == 404:
        print(f"Licence key not found: {licence_key}")
    else:
        print("Failed to connect to the licensing server.")


if __name__ == '__main__':
    licence_key = input("Enter your licence key: ")
    get_licence(licence_key)
