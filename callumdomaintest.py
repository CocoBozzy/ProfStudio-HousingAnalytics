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


def suburbPerformance(token, suburb, postcode, bedrooms):
    url = 'https://api.domain.com.au/v2/suburbPerformanceStatistics/NSW/' + suburb + '/' + str(postcode) + '?bedrooms=' + str(bedrooms) +'&periodSize=years&startingPeriodRelativeToCurrent=1&totalPeriods=11'

    auth = {'Authorization': 'Bearer ' + token}

    resp = requests.get(url, headers=auth)
    print(resp.status_code)
    resp_json = resp.json()
    return resp_json


def extract_sold_in_year(json_response):
    info = json_response['series']['seriesInfo']
    print(json.dumps(info, indent=4))

    yearSalesResultDict = {}
    for i in info:
        yearSalesResultDict[i['year']] = i['values']['numberSold']

    print(json.dumps(yearSalesResultDict, indent=4))
    return yearSalesResultDict


def get_sales_per_suburb_per_year(token, suburb, postcode, bedrooms):
    json_response = suburbPerformance(token, suburb, postcode, bedrooms)
    json_response = extract_sold_in_year(json_response)
    return json_response


if __name__ == '__main__':
    token = get_access_token()
    # result = suburbPerformance(token, suburb='Avalon Beach', postcode=2107, bedrooms=4)
    test = get_sales_per_suburb_per_year(token, suburb='Avalon Beach', postcode=2107, bedrooms=4)
    print(test)
