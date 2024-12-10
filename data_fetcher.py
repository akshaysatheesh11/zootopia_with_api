import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.api-ninjas.com/v1/animals?name="  

def fetch_data(animal_name):
    """
    Fetches animal data from the API using the animal_name.
    Returns a list of animals.
    """
    headers = {
        'X-Api-Key': API_KEY
    }
    
    response = requests.get(BASE_URL + animal_name, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the fetched data as JSON
    else:
        return None  # Return None if the API call failed
