import requests
import json

def turn_on_lights():
    # Replace the API key and device ID with your own
    api_key = "YOUR_API_KEY"
    device_id = "YOUR_DEVICE_ID"
    url = f"https://api.smart-home.com/v1/devices/{device_id}/on"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Make the API call to turn on the device
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Lights turned on successfully!")
    else:
        print("Error turning on lights.")

def turn_off_lights():
    # Replace the API key and device ID with your own
    api_key = "YOUR_API_KEY"
    device_id = "YOUR_DEVICE_ID"
    url = f"https://api.smart-home.com/v1/devices/{device_id}/off"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Make the API call to turn off the device
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Lights turned off successfully!")
    else:
        print("Error turning off lights.")
