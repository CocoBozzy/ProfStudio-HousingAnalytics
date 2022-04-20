import requests
import json
from DataCollection import convert_to_df

rach_client = ''
rach_secret = ''
rach_api_key = ''
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


def get_agencies_listings(token):
    auth = {'Authorization': 'Bearer ' + token}
    listing_url = listing_base_url + 'residential/_search'
    print(listing_url)

    data = {
        'listingType': 'Sale',
        'minBedrooms': 2,
        'minBathrooms': 1,
        'minCarspaces': 1,
        "locations": [
            {
                "state": "NSW",
                "region": "",
                "area": "",
                "suburb": "Deewhy",
                "postCode": "",
                "includeSurroundingSuburbs": False
            }]
    }

    resp = requests.post(listing_url, headers=auth, data=json.dumps(data))
    resp_json = resp.json()
    print(resp_json)
    return resp_json


# TODO get ids to put in url so they aren't just static
# TODO get user to enter in their use case - residential, business or commercial -
#  https://developer.domain.com.au/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialsearch


if __name__ == "__main__":
    token = get_access_token()
    dicts = get_agencies_listings(token)
    df = convert_to_df.convert_dict_to_df(dicts)
    print(df)
