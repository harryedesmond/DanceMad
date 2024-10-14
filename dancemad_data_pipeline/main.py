import pandas as pd
import numpy as np
import sys
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Allows to use my own packages from my project directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from collect_data.google_places import get_google_places
from collect_data.yelp_fusion import get_yelp_fusion

# -----------------------------Basic Info -------------------------------

dance_types = ['Salsa', 'Bachata']
city = ['New York', 'London', 'Warsaw', 'Madrid', 'Barcelona', 'Paris', 'Lima', 'Rio de Janiero', 'Cali, Colombia', 'Buenos Aires']


# ------------- Gather Data from API's

# Setup DataFrame for Google data
google_columns= ['name', 'formatted_address', 'rating', 'user_ratings_total', 'types', 'price_level']
columns = google_columns + ['dance_type', 'city']
google_df = pd.DataFrame([], columns =columns)

g_save = True # 

# Setup yelp_columns for Yelp data
yelp_columns = ['name', 'location', 'categories', 'rating', 'review_count']
columns = yelp_columns + ['dance_type', 'city']
yelp_df = pd.DataFrame([], columns =columns)

y_save = True # 

# Details
google_api_key = os.getenv('GOOGLE_API_KEY')

# search each dance style
for style in dance_types:
    for city_name in city:
        
        # Gather data from Google Places --------------------------------------
        g_data = get_google_places(google_api_key, city_name, style)
        
        # Add data from google to df                
        if isinstance(g_data, type(None)) == False: # Checks that some data has been loaded
            for place in g_data:
                new_row = {col: place.get(col, np.nan) for col in google_columns} # if column missing from data fill it with np.nan
                new_row.update({'dance_type': style, 'city': city_name})
                
                google_df.loc[len(google_df)] = new_row
                
        else:
            g_save = False
        
        # Gather Yelp Fusion data ---------------------------------------------
        y_data = get_yelp_fusion(city_name, style)
        
        if isinstance(y_data, type(None)) == False: # Checks that some data has been loaded
            # Add data from google to df                   
            for place in y_data:
                new_row = {col: place.get(col, np.nan) for col in yelp_columns} # if column missing from data fill it with np.nan
                new_row.update({'dance_type': style, 'city': city_name})
                
                yelp_df.loc[len(yelp_df)] = new_row
                
        else:
            y_save = False
            

# Save dataframes 
# if g_save != False:
google_df.to_csv('C:/Users/hazze/OneDrive/Documents/DanceMad/dancemad_data_pipeline/process_data/google_data.csv')
# if y_save != False:
yelp_df.to_csv('C:/Users/hazze/OneDrive/Documents/DanceMad/dancemad_data_pipeline/process_data/yelp_data.csv')          