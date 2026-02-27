import pandas as pd


def my_data():
    url_main = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
    url1 = url_main + '/time_series_covid19_confirmed_global.csv'
    url2 = url_main + '/time_series_covid19_deaths_global.csv'
    url3 = url_main + '/time_series_covid19_recovered_global.csv'

    list_url = [url1, url2, url3]

    for i in list_url:
        df = pd.read_csv(i)
        df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
        df = df.set_index('Country/Region')

        if i == url1:
            df_confirmed = df

        elif i == url2:
            df_deaths = df

        elif i == url3:
            df_recovered = df

        else:
            pass

    return {'Confirmados': df_confirmed,
            'Muertos': df_deaths,
            'Recuperados': df_recovered}
