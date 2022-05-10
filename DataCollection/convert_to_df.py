import pandas as pd
import numpy as np

# test
# edit the format of data in the df
def convert_dict_to_df(dicts):
    ListingID = []
    ListingType = []
    AdvertiserID = []
    AdvertiserType = []
    AdvertiserName = []
    DisplayPrice = []
    State = []
    PropertyType = []
    Bathrooms = []
    Bedrooms = []
    Carspaces = []
    UnitNumber = []
    StreetNumber = []
    Street = []
    Area = []
    Suburb = []
    Postcode = []
    Latitude = []
    Longitude = []
    BuildingArea = []
    IsRural = []
    IsNew = []
    Headline = []
    SummaryDescription = []
    DateListed = []
    AuctionTime = []

    # print(df)
    # dicts[0].listing.listingType.id.advertiser.type.advertiser.id.advertiser.name.priceDetails.displayPrice
    # all of.propertyDetails.headline.summaryDescription.dateListed.auctionSchedule.time

    for dict in dicts:
        try:
            ListingID.append(dict['listing']['id'])
        except:
            ListingID.append(np.nan)
        try:
            ListingType.append(dict['listing']['listingType'])
        except:
            ListingType.append(np.nan)
        try:
            AdvertiserID.append(dict['listing']['advertiser']['id'])
        except:
            AdvertiserID.append(np.nan)
        try:
            AdvertiserType.append(dict['listing']['advertiser']['type'])
        except:
            AdvertiserType.append(np.nan)
        try:
            AdvertiserName.append(dict['listing']['advertiser']['name'])
        except:
            AdvertiserName.append(np.nan)
        try:
            DisplayPrice.append(dict['listing']['priceDetails']['displayPrice'])
        except:
            DisplayPrice.append(np.nan)
        try:
            State.append(dict['listing']['propertyDetails']['state'])
        except:
            State.append(np.nan)
        try:
            PropertyType.append(dict['listing']['propertyDetails']['propertyType'])
        except:
            PropertyType.append(np.nan)
        try:
            Bathrooms.append(dict['listing']['propertyDetails']['bathrooms'])
        except:
            Bathrooms.append(np.nan)
        try:
            Bedrooms.append(dict['listing']['propertyDetails']['bedrooms'])
        except:
            Bedrooms.append(np.nan)
        try:
            Carspaces.append(dict['listing']['propertyDetails']['carspaces'])
        except:
            Carspaces.append(np.nan)
        try:
            UnitNumber.append(dict['listing']['propertyDetails']['unitNumber'])
        except:
            UnitNumber.append(np.nan)
        try:
            StreetNumber.append(dict['listing']['propertyDetails']['streetNumber'])
        except:
            StreetNumber.append(np.nan)
        try:
            Street.append(dict['listing']['propertyDetails']['street'])
        except:
            Street.append(np.nan)
        try:
            Area.append(dict['listing']['propertyDetails']['area'])
        except:
            Area.append(np.nan)
        try:
            Suburb.append(dict['listing']['propertyDetails']['suburb'])
        except:
            Suburb.append(np.nan)
        try:
            Postcode.append(dict['listing']['propertyDetails']['postcode'])
        except:
            Postcode.append(np.nan)
        try:
            Latitude.append(dict['listing']['propertyDetails']['latitude'])
        except:
            Latitude.append(np.nan)
        try:
            Longitude.append(dict['listing']['propertyDetails']['longitude'])
        except:
            Longitude.append(np.nan)
        try:
            BuildingArea.append(dict['listing']['propertyDetails']['buildingArea'])
        except:
            BuildingArea.append(np.nan)
        try:
            IsRural.append(dict['listing']['propertyDetails']['isRural'])
        except:
            IsRural.append(np.nan)
        try:
            IsNew.append(dict['listing']['propertyDetails']['isNew'])
        except:
            IsNew.append(np.nan)
        try:
            Headline.append(dict['listing']['headline'])
        except:
            Headline.append(np.nan)
        try:
            SummaryDescription.append(dict['listing']['summaryDescription'])
        except:
            SummaryDescription.append(np.nan)
        try:
            DateListed.append(dict['listing']['dateListed'])
        except:
            DateListed.append(np.nan)
        try:
            AuctionTime.append(dict['listing']['auctionSchedule']['time'])
        except:
            AuctionTime.append(np.nan)

    df = pd.DataFrame({
        'ListingID': ListingID,
        'ListingType': ListingType,
        'AdvertiserID': AdvertiserID,
        'AdvertiserType': AdvertiserType,
        'AdvertiserName': AdvertiserName,
        'DisplayPrice': DisplayPrice,
        'State': State,
        'PropertyType': PropertyType,
        'Bathrooms': Bathrooms,
        'Bedrooms': Bedrooms,
        'Carspaces': Carspaces,
        'UnitNumber': UnitNumber,
        'StreetNumber': StreetNumber,
        'Street': Street,
        'Area': Area,
        'Suburb': Suburb,
        'Postcode': Postcode,
        'Latitude': Latitude,
        'Longitude': Longitude,
        'BuildingArea': BuildingArea,
        'IsRural': IsRural,
        'IsNew': IsNew,
        'Headline': Headline,
        'SummaryDescription': SummaryDescription,
        'DateListed': DateListed,
        'AuctionTime': AuctionTime
    })

    return df