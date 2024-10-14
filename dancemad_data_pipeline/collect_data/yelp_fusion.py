import requests

# Yelp API base URL
url = 'https://api.yelp.com/v3/businesses/search'
yelp_api_key = 'dvtPmErwVqX_DCn62q8lEc-VG4hLhOX0TtVdAJfuVT0DAsus0EyPwphl4-9I3QK2LNZDS9t03455ad360hKqDbrC3jYY45B-RVvzdXPkm0f7-hsU4B8eI92sUmjbZnYx'

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
