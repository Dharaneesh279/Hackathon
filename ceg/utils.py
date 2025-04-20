# utils.py or another appropriate file in your Django app directory
import requests

# Define your ThingSpeak channel and read API key
THINGSPEAK_CHANNEL_ID = '2756474'
READ_API_KEY = '3XGCUU9NH3ATULEB'

# Function to get data from ThingSpeak API
def get_thingspeak_data():
    url = f'https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds.json?results=2'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # returns data as a dictionary
    else:
        return None


