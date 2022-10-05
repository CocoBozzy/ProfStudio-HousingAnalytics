import requests
import json

cal_client = 'client_f49317aa4d716d953f138865e1f399d9'
cal_secret = 'secret_dcffc2565d1043fd13ac488f3e522296'
auth_url = 'https://auth.domain.com.au/v1/connect/token'
url_test = 'https://api.domain.com.au/v1/agencies/22473/listings?listingStatusFilter=live&pageNumber=1&pageSize=3'
listing_base_url = 'https://api.domain.com.au/v1/listings/'


def get_access_token():
    resp = requests.post(auth_url, data={
        'client_id': cal_client,
        'client_secret': cal_secret,
        'scope': 'api_suburbperformance_read',
        'grant_type': 'client_credentials',
        'Content-Type': 'text/json'
    })
    json_resp = resp.json()
    access_token = json_resp['access_token']
    print(access_token)
    return access_token


def get_salesResults(token , suburb = 'Sydney'):
    
    url = 'https://api.domain.com.au/v1/salesResults/Sydney/listings'
    
    auth = {'Authorization': 'Bearer ' + token}
    
    resp = requests.get(url, headers=auth)
    print(resp.status_code)
    resp_json = resp.json()
    # print(json.dumps(resp_json, indent=4))
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

######################################################################################################################################

def suburbPerformance(token, propertyCategory, bedrooms, state, suburb, postcode):
    
    url = 'https://api.domain.com.au/v2/suburbPerformanceStatistics/' + state +'/' + suburb +'/' + str(postcode) + '?propertyCategory=' +  propertyCategory + '&bedrooms=' + str(bedrooms) +'&periodSize=years&startingPeriodRelativeToCurrent=1&totalPeriods=11'
    
    auth = {'Authorization': 'Bearer ' + token}
    
    
    resp = requests.get(url, headers=auth)
    print(resp.status_code)
    resp_json = resp.json()
    # print(json.dumps(resp_json, indent=4))
    return resp_json
    
def extract_sold_in_year(json_response):
    info = json_response['series']['seriesInfo']
    print(json.dumps(info, indent=4))

    yearSalesResultDict = {}
    for i in info:
        yearSalesResultDict[i['year']] = i['values']['numberSold']
        
    print(json.dumps(yearSalesResultDict, indent=4))
    return yearSalesResultDict


def get_sales_per_suburb_per_year(token, propertyCategory, bedrooms, state, suburb, postcode):
    json_response = suburbPerformance(token, propertyCategory, bedrooms, state, suburb, postcode)
    extract_sold_in_year(json_response)
    
    

if __name__ == '__main__':
    token = get_access_token()
    get_sales_per_suburb_per_year(token, propertyCategory='house', bedrooms=4, state='nsw', suburb='terrigal', postcode=2260)

    

