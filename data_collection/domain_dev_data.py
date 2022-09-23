import requests
import json
import folium
import pandas as pd
from data_collection import convert_to_df

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


# TODO get ids to put in url so they aren't just static
# TODO get user to enter in their use case - residential, business or commercial -
#  https://developer.domain.com.au/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialsearch


if __name__ == "__main__":
    token = get_access_token()
    dicts = get_agencies_listings(token, "Newtown")
    df = convert_to_df.convert_dict_to_df(dicts)
    print(df)

    # visualisations
    locations = df[['Latitude', 'Longitude']]
    location_list = locations.values.tolist()
    len(location_list)
    print(location_list[0])

    map = folium.Map(location=location_list[0], zoom_start=12)
    try:
        for point in range(0, len(location_list)):
            folium.Marker(location_list[point], popup=df['ListingType'][point]).add_to(map)
    except:
        print('')
    map.save('my_map2.html')
