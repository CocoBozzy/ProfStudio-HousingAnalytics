import pandas as pd


def clean_school_data():
    df = pd.read_csv('../data_sources/datasource-NSW-Gov-DE-school-locations.csv')

    # columns I need: school_name, level_of_schooling, school_gender, suburb, latitude, longitude
    df_new = df[['school_name', 'level_of_schooling', 'school_gender', 'suburb', 'latitude', 'longitude']]
    df_new.to_csv('../data_sources/school-locations-clean.csv')


if __name__ == "__main__":

    df_schools = pd.read_csv('../data_sources/school-locations-clean.csv')
    df_schools = df_schools[df_schools['suburb'] == 'North Narrabeen']
    school_locations = df_schools[['latitude', 'longitude']]
    school_locations_list = school_locations.values.tolist()

    print(df_schools)
