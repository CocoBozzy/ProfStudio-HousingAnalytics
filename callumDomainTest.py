import requests
import json

rach_client = 'client_e4658c392bc206a4e6dfb1335576444b'
rach_secret = 'secret_830a73c26ec95dc66c2d605e62809e08'
rach_api_key = 'key_54d3141d923ee3353eab7288845f9f82'
auth_url = 'https://auth.domain.com.au/v1/connect/token'
url_test = 'https://api.domain.com.au/v1/agencies/22473/listings?listingStatusFilter=live&pageNumber=1&pageSize=3'
listing_base_url = 'https://api.domain.com.au/v1/listings/'


def get_access_token():
    resp = requests.post(auth_url, data={
        'client_id': rach_client,
        'client_secret': rach_secret,
        'scope': 'api_listings_read',
        'grant_type': 'client_credentials',
        'Content-Type': 'text/json'
    })
    json_resp = resp.json()
    access_token = json_resp['access_token']
    print(access_token)
    return access_token


def get_salesResults(token , suburb = 'Sydney'):
    
    url = 'https://api.domain.com.au/v1/salesResults/' + suburb
    
    auth = {'X-Api-Key': token}
    
    resp = requests.get(url, headers=auth)
    print(resp.status_code)
    resp_json = resp.json()
    print(resp_json)
    return resp_json


def get_agencies_listings(token, suburb, bedrooms=1, bathrooms=1, cars=1):
    auth = {'Authorization': 'Bearer ' + token}
    listing_url = listing_base_url + 'residential/_search'
    print(listing_url)

    data = {
        'listingType': 'Sale',
        'minBedrooms': bedrooms,
        'minBathrooms': bathrooms,
        'minCarspaces': cars,
        "locations": [
            {
                "state": "NSW",
                "region": "",
                "area": "",
                "suburb": '"' + suburb + '"',
                "postCode": "",
                "includeSurroundingSuburbs": False
            }
        ]
    }
    print(data)

    resp = requests.post(listing_url, headers=auth, data=json.dumps(data))
    resp_json = resp.json()
    print(resp_json)
    return resp_json

if __name__ == '__main__':
    token = 'key_7a95da6a34c2d3c8b213bd5430f3016d'
    get_salesResults(token)