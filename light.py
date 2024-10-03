import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Replace with your ESP8266 IP address
esp_ip = os.getenv("IP")


def light_on():
    try:
        response = requests.get(esp_ip + 'on')
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def light_off():
    try:
        response = requests.get(esp_ip + 'off')
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


# Example usage
# print(light_on())  # Turn on the LED
# light_off()  # Turn off the LED
