import pandas as pd
import numpy as np


def snap_top(data):

    for i, k in zip(data.values(), data.keys()):

        df = i
        df = df.iloc[:, -1:]
        df['Value'] = df.iloc[:, -1]
        df = df.drop(df.columns[0], axis=1)
        df = df.groupby(['Country/Region']).sum()
        df = df.reset_index()

        if k == 'Confirmados':
            df = df.rename(columns={"Value": "ValueConf"})
            confirmed_snap = df

        elif k == 'Muertos':
            df = df.rename(columns={"Value": "ValueDeaths"})
            deaths_snap = df

        elif k == 'Recuperados':
            df = df.rename(columns={"Value": "ValueRecover"})
            recovered_snap = df

        else:
            pass

    merge1 = confirmed_snap.merge(deaths_snap, on='Country/Region')
    merge2 = merge1.merge(recovered_snap, on='Country/Region')
    merge2 = merge2.sort_values(by='ValueConf', ascending=False)

    # Index table
    frame = merge2
    frame = frame.reset_index(drop=True)
    frame = frame.reset_index()
    frame['RateDeath'] = round(frame['ValueDeaths']/frame['ValueConf']*100, 3)
    frame['RateRecover'] = round(frame['ValueRecover']/frame['ValueConf']*100, 3)
    frame['RateDeath'] = frame['RateDeath'].astype(str) + ' %'
    frame['RateRecover'] = frame['RateRecover'].astype(str) + ' %'

    # top
    merge2 = merge2.iloc[:10]
    merge2 = merge2.reset_index(drop=True)
    merge2 = merge2.reset_index()
    merge2['RateDeath'] = round(merge2['ValueDeaths']/merge2['ValueConf']*100, 3)
    merge2['RateRecover'] = round(merge2['ValueRecover']/merge2['ValueConf']*100, 3)
    merge2['RateDeath'] = merge2['RateDeath'].astype(str) + ' %'
    merge2['RateRecover'] = merge2['RateRecover'].astype(str) + ' %'
    # convert to array
    ds1 = np.array(merge2['ValueConf'])
    ds2 = np.array(merge2['ValueRecover'])
    ds3 = np.array(merge2['ValueDeaths'])

    return [merge2, ds1, ds2, ds3, frame]


def arg_stats(data):
    for i, j in zip(data.values(), data.keys()):
        i = i.T
        i['Date'] = i.index
        i = i[['Argentina', 'Date']]
        i['Date'] = pd.to_datetime(i['Date'])
        i['Index_Date'] = i['Date']
        i = i.set_index('Index_Date')

        # ##################### Media valores por dia #########################
        df_md_day = i[i['Argentina'] > 0]

        lista = list(df_md_day['Argentina'])
        lista2 = list(df_md_day['Argentina'])

        n1 = lista[0:]
        n2 = lista2[1:]

        n3 = []

        for k, l in zip(n1, n2):
            add = l - k
            n3.append(add)

        if j == 'Confirmados':
            media_dia_confir = int(np.mean(n3))
        elif j == 'Muertos':
            media_dia_muerto = int(np.mean(n3))
        elif j == 'Recuperados':
            media_dia_recup = int(np.mean(n3))
        else:
            pass
        #######################################################################

        df_last_day = i.iloc[-1]

        i = i[(i.index + pd.Timedelta(days=1)).day == 1]
        i = i.append(df_last_day)

        i['Date'] = i['Date'].dt.strftime('%Y-%m')

        if j == 'Confirmados':
            i = i.rename(columns={"Argentina": "Confirmados"})
            df_confirmed = i

        elif j == 'Muertos':
            i = i.rename(columns={"Argentina": "Muertos"})
            df_deaths = i

        elif j == 'Recuperados':
            i = i.rename(columns={"Argentina": "Recuperados"})
            df_recovered = i

        else:
            pass

    df = df_confirmed.merge(df_deaths, on='Date')
    df = df.merge(df_recovered, on='Date')

    df['RateDeath'] = round(df['Muertos']/df['Confirmados']*100, 3)
    df['RateRecover'] = round(df['Recuperados']/df['Confirmados']*100, 3)
    df = df.fillna(0)

    # ######### Media valroes #############################################

    df = df[['Confirmados',
             'Muertos',
             'Recuperados',
             'RateDeath',
             'RateRecover',
             'Date']]

    cols = list(df.iloc[:, :-1].columns)

    for q in cols:
        df_mean = df[df[q] > 0]
        lista1 = list(df_mean[q])
        lista2 = list(df_mean[q])

        n1 = lista1[0:]
        n2 = lista2[1:]

        lista_val = []

        for k, l in zip(n1, n2):
            add = l - k
            lista_val.append(add)

        if q == 'Confirmados':
            media_mes_confir = int(np.mean(lista_val))
        elif q == 'Muertos':
            media_mes_muertes = int(np.mean(lista_val))
        elif q == 'Recuperados':
            media_mes_recupe = int(np.mean(lista_val))

    ###########################################################################

    df['RateDeath'] = df['RateDeath'].astype(str) + ' %'
    df['RateRecover'] = df['RateRecover'].astype(str) + ' %'

    return [df,
            media_dia_confir,
            media_dia_muerto,
            media_dia_recup,
            media_mes_confir,
            media_mes_muertes,
            media_mes_recupe]
