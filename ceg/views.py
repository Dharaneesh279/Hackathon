from django.shortcuts import render
import requests  # Import requests to fetch data from ThingSpeak

# Define your ThingSpeak channel and read API key
THINGSPEAK_CHANNEL_ID = '2756474'
READ_API_KEY = '3XGCUU9NH3ATULEB'

# Function to fetch data from ThingSpeak
def get_thingspeak_data():
    url = f'https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds.json?results=2'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # returns data as a dictionary
    else:
        return None

# View to render the dashboard
def db(request):
    data = get_thingspeak_data()  # Fetch data from ThingSpeak API
    
    if data:
        # Process the data as needed
        feeds = data['feeds']
        
        # Assuming field2 is for Voltage, field3 is for Current
        voltage_data = [feed['field2'] for feed in feeds if feed['field2'] is not None]  # Extract voltage data (field2)
        current_data = [feed['field3'] for feed in feeds if feed['field3'] is not None]  # Extract current data (field3)
        
        # Pass data to the template
        return render(request, 'dashboard.html', {
            'voltage_data': voltage_data,
            'current_data': current_data,
        })
    else:
        return render(request, 'dashboard.html', {
            'error': 'Unable to fetch data from ThingSpeak'
        })

# Other views
def tab(request):
    return render(request, 'tables.html')

def noti(request):
    return render(request, 'notifications.html')

def watertracking(request):
    return render(request, 'Watertracking.html')
