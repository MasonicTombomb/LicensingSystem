import requests
from datetime import datetime
import hashlib
import platform
import psutil


def getLicence(licence_key):
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


def getUniqueID():
    # Get MAC addresses of all network interfaces
    mac_addresses = []
    for interface, addresses in psutil.net_if_addrs().items():
        for address in addresses:
            if address.family == psutil.AF_LINK:
                mac_addresses.append(address.address)

    # Get system information
    system_info = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()

    # Combine MAC addresses and system information into a unique string
    unique_string = ''.join(mac_addresses) + system_info + node + release + version

    # Generate a unique hash using SHA-256
    unique_hash = hashlib.sha256(unique_string.encode()).hexdigest()

    # Combine with a random UUID to add more uniqueness
    unique_id = f"{unique_hash}"

    return unique_id




if __name__ == '__main__':
    licence_key = input("Enter your licence key: ")
    getLicence(licence_key)
