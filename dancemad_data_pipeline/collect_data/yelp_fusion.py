import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Yelp API base URL
url = 'https://api.yelp.com/v3/businesses/search'
yelp_api_key = os.getenv('YELP_API_KEY') 

# Set the API request headers
headers = {
    'Authorization': f'Bearer {yelp_api_key}',
}

def get_yelp_fusion(location, style, limit=10):
    """Search Yelp for dance venues in a specific location."""
    
    params = {
        'term': style + ' dance club',           # Search term, e.g., 'Salsa dance club'
        'location': location,   # The location to search for, e.g., 'New York'
        'limit': limit,         # Limit the number of results returned (max is 50)
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()['businesses']
    else:
        print(f"Error: {response.status_code}")
        return None
