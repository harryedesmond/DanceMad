import requests

def get_google_places(api_key, city, dance_type):
    
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={dance_type}+dance+clubs+in+{city}&key={api_key}"

    response = requests.get(url)  
    
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error: {response.status_code}")
        return None
   