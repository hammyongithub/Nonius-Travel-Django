# curl "https://test.api.amadeus.com/v1/security/oauth2/token"      -H "Content-Type: application/x-www-form-urlencoded"      -d "grant_type=client_credentials&client_id=UgvkvcINTG93c4hNbGGY4LN3nRxrk9Ex&client_secret=TZLqA7rukbLdWSSw"

#         {
#             "type": "amadeusOAuth2Token",
#             "username": "jorge@domingues.tech",
#             "application_name": "demoamadeushotel",
#             "client_id": "UgvkvcINTG93c4hNbGGY4LN3nRxrk9Ex",
#             "token_type": "Bearer",
#             "access_token": "UeBbIzOk8ip5Mv1sAggBay8C1gQv",
#             "expires_in": 1799,
#             "state": "approved",
#             "scope": ""
#         }

# GET EXAMPLE:  curl "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city?cityCode=LON"      -H "Authorization: Bearer RMvQjG3TK1ixyYXf2DG6dnVqprUx"


from tabnanny import check
from unittest import result
from venv import logger
import requests
import time
import logging

logger = logging.getLogger(__name__)

# Define your client credentials
CLIENT_ID = 'UgvkvcINTG93c4hNbGGY4LN3nRxrk9Ex'
CLIENT_SECRET = 'TZLqA7rukbLdWSSw'

# Initialize variables to store the access token and its expiration time
ACCESS_TOKEN = None
TOKEN_EXPIRATION = 0

# Function to obtain or refresh the access token
def get_access_token():
    global ACCESS_TOKEN, TOKEN_EXPIRATION
    current_time = int(time.time())

    # Check if the token is expired or not obtained yet
    if ACCESS_TOKEN is None or current_time >= TOKEN_EXPIRATION:
        token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            token_data = response.json()
            ACCESS_TOKEN = token_data['access_token']
            TOKEN_EXPIRATION = current_time + token_data['expires_in']
        else:
            # Handle token retrieval error
            raise Exception("Failed to retrieve access token")

    return ACCESS_TOKEN

# Function to make authenticated API requests
def make_authenticated_request(url, params=None):
    headers = {
        'Authorization': f'Bearer {get_access_token()}',
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors gracefully
        return None

def search_hotels(location):
    base_url = 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city'
    params = {
        'cityCode': location,  # City or location code,
    }

    result = make_authenticated_request(base_url, params=params)

    return result


def search_offers(hotelIds, adults, checkInDate, checkOutDate, roomQuantity, priceRange, currency, boardType):
    base_url = 'https://test.api.amadeus.com/v3/shopping/hotel-offers'
    
    params = {
        'hotelIds': hotelIds,
        'adults': adults,
        'checkInDate': checkInDate,
        'checkOutDate': checkOutDate,
        'roomQuantity': roomQuantity,
        'priceRange': priceRange,
        'currency': currency,
        'boardType': boardType,
    }

    result = make_authenticated_request(base_url, params=params)

    return result