import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# removes dirty data
def removedirty():
    df = pd.read_csv('dirty_data.csv')

    # Renames the first column as it is named unnamed.

    df.rename(columns={'Unnamed: 0': 'ID'}, inplace=True)
    print(df)
# removes dirty uber type :
    for i, j in df.iterrows():
        if j['Uber Type'] > 2:
            if str(j.ID)[2:3] == '1':
                df.loc[i, ['Uber Type']] = 0
            elif str(j.ID)[2:3] == '3':
                df.loc[i, ['Uber Type']] = 1
            elif str(j.ID)[2:3] == '5':
                df.loc[i, ['Uber Type']] = 2
        else:
            if str(j.ID)[2:3] == '1':
                if j['Uber Type'] != 0:
                    df.loc[i, ['Uber Type']] = 0
            elif str(j.ID)[2:3] == '3':
                if j['Uber Type'] != 1:
                    df.loc[i, ['Uber Type']] = 1
            elif str(j.ID)[2:3] == '5':
                if j['Uber Type'] != 2:
                    df.loc[i, ['Uber Type']] = 2
    # print(df)
    # r = list(df['Origin Region'])
    # ut = list(df['Uber Type'])
    # plt.scatter(ut, r)
    # r = list(df['Origin Latitude'])
    # ut = list(df['Origin Longitude'])
    # plt.scatter(ut, r)
    c = 0
    # plt.hist(df['Origin Latitude'], bins = 20)
    # plt.show()
    la = list()


# Finds the dirty values in the Latitude and Longitude Columns and also removes the error
    def Latcorrect(key):
        la = list()
        for i in list(df[key]):
            if i > 0:
                la.append(-i)
            else:
                la.append(i)
        return la

    la = Latcorrect('Origin Latitude')
    df['Origin Latitude'] = la
    la = list()
    la = Latcorrect('Destination Latitude')
    df['Destination Latitude'] = la

# removes dirty dates
    dates = []
    for i in range(df['Departure Date'].__len__()):
        dates.append(list(df['Departure Date'])[i].split('-'))
    months = []
    date = []
    for i in range(dates.__len__()):
        if int(dates[i][1]) > 12:
            dates[i][1], dates[i][2] = dates[i][2], dates[i][1]
        if int(dates[i][2]) > 31:
            dates[i][1], dates[i][2] = dates[i][2], dates[i][1]
        if (int(dates[i][1]) == 1 or int(dates[i][1]) == 3 or int(dates[i][1]) == 5 or int(dates[i][1]) == 7 or int(dates[i][1]) == 8 or int(dates[i][1]) == 10 or int(dates[i][0]) == 12) and int(dates[i][2]) > 31:
            dates[i][2] = '31'
        elif int(dates[i][1]) == 2 and int(dates[i][2]) > 28:
            dates[i][2] = '28'
        elif (int(dates[i][1]) == 4 or int(dates[i][1]) == 6 or int(dates[i][1]) == 9 or int(dates[i][1]) == 11) and int(dates[i][2]) > 30:
            dates[i][2] = '30'
        months.append(dates[i][1])
        date.append(dates[i][2])
    fd = []
    for i in range(dates.__len__()):
        fd.append(str(dates[i][2]) + "-" + str(dates[i][1]) + "-" + str(dates[i][0]))

    df['Departure Date'] = fd
# removes dirty time
    minu = []
    sec = []
    timesd = []
    for i in range(df['Departure Time'].__len__()):
        timesd.append(list(df['Departure Time'])[i].split(':'))
    secd = []
    mind = []
    timesa = []
    for i in range(df['Arrival Time'].__len__()):
        timesa.append(list(df['Arrival Time'])[i].split(':'))
    tra = []
    for i in range(df['Travel Time(s)'].__len__()):
        tra.append(list(df['Travel Time(s)'])[i])
    seca = []
    mina = []
    diff = 0
    secondsa1 = 0
    secondsd = 0
    ea = []
    eb = []
    arri = []
    a = 0
    travel = []
    for i in range(tra.__len__()):
        travel.append(0)
    for i in range(timesd.__len__()):
        if int(timesd[i][1]) >= 60:
            timesd[i][1] = '59'
        if int(timesa[i][1]) >= 60:
            timesa[i][1] = '59'
        if int(timesd[i][2]) >= 60:
            timesd[i][2] = '59'
        if int(timesa[i][2]) >= 60:
            timesa[i][2] = '59'
        if int(timesd[i][0]) >= 24:
            timesd[i][0] = '23'
        if int(timesa[i][0]) >= 24:
            timesa[i][0] = '23'
        dis  = list(df['Journey Distance(m)'])
        secondsd = (int(timesd[i][0])*60*60 + int(timesd[i][1])*60) + int(timesd[i][2])
        secondsa = (int(timesa[i][0])*60*60 + int(timesa[i][1])*60) + int(timesa[i][2])
        diff = (secondsa - secondsd) - tra[i]
        ea.append(diff)
        travel[i] = tra[i]
        if abs(dis[i]/abs(secondsa - secondsd)*18/5) < 10:
            secondsa = abs(secondsa - abs(diff))
            travel[i] = abs(secondsa - secondsd)
            c = 0
            c = secondsa
            timesa[i][2] = c % 60
            a = c // 60
            timesa[i][1] = a % 60
            c = a // 60
            timesa[i][0] = c % 24
        diff = (secondsa - secondsd) - tra[i]
        arri.append([str(int(timesa[i][0])) + ":" + str(int(timesa[i][1])) + ":" + str(int(timesa[i][2]))])
        eb.append(diff)
    df['Arrival Time'] = arri
    df['Travel Time(s)'] = travel
    print(df)
    # plt.hist(ea, bins=20)
    # plt.show()
    # plt.hist(eb, bins=20)
    # plt.show()
    df.to_csv('_dirty_data_solution.csv')

removedirty()


def outliers():
    out = pd.read_csv('outliers.csv')
# removes outliers in Orgin latitude and origin longitude
    lat = list(out['Origin Latitude'])
    long = list(out['Origin Longitude'])
    lan = np.array(lat)
    lon = np.array(long)
    lam = np.mean(lan)
    lom = np.mean(lon)
    lo = []
    la = []
    las = np.std(lan)
    los = np.std(lon)
    for i, j in out.iterrows():
        if abs(j['Origin Latitude'] - lam) > las*2:
            la.append(i)
        if abs(j['Origin Longitude']- lom) > los*2:
            lo.append(i)
    for i in la:
        out = out.drop(i)
    print(out)
# removes outliers in Destination latitude and Destination longitude
    lat = list(out['Destination Latitude'])
    long = list(out['Destination Longitude'])
    lan = np.array(lat)
    lon = np.array(long)
    lam = np.mean(lan)
    lom = np.mean(lon)
    lo = []
    la = []
    las = np.std(lan)
    los = np.std(lon)
    for i, j in out.iterrows():
        if abs(j['Destination Latitude'] - lam) > las*2:
            la.append(i)
        if abs(j['Destination Longitude']- lom) > los*2:
            lo.append(i)
    for i in la:
        out = out.drop(i)
    out.rename(columns={'Unnamed: 0': 'IDa'}, inplace=True)
    out = out.drop('IDa', axis=1)
    out.rename(columns={'Unnamed: 0.1': 'ID'}, inplace=True)
    print(out)
    # plt.scatter(lat, long)
    # plt.show()
    out.to_csv('_outliers_solution.csv')

outliers()

def misingvalues():
    df = pd.read_csv('missing_value.csv')
    df.rename(columns={'Unnamed: 0': 'ID'}, inplace=True)
    print(df)
# identifies and replaces the mising values in uber type column
    for i, j in df.iterrows():
        if pd.isna(j['Uber Type']):
            if str(j['ID'])[2:3] == '5':
                df.loc[i, ['Uber Type']] = 2
            if str(j['ID'])[2:3] == '3':
                df.loc[i, ['Uber Type']] = 1
            if str(j['ID'])[2:3] == '1':
                df.loc[i, ['Uber Type']] = 0
    print(df)
    fg = []
# identifies and removes the missing values in fares
    l = df['Fare$'].isna()
    dg = []
    for i in range(l.__len__()):
        if l[i]:
            dg.append(df.loc[i, 'Journey Distance(m)'])
            fg.append(df.loc[i, 'Uber Type'])
    f = []
    d = []
    e = []
    for i in range(l.__len__()):
        if not l[i]:
            d.append(df.loc[i, 'Journey Distance(m)'])
            f.append(df.loc[i, 'Uber Type'])
            e.append(df.loc[i, 'Fare$'])
    df1 = pd.DataFrame({'Journey Distance(m)': d, 'Uber Type':f,'Fare$': e})
    from sklearn import linear_model
    find = list()

# this function predicts the fare values using the already given Journey distance and uber type values
# using LinerRegression model.

    def Linear(dep, indepen, i):
        rg = linear_model.LinearRegression()
        rg.fit(df1[[dep[0], dep[1]]], df1[indepen[0]])
        b = rg.predict([[dg[i], fg[i]]])
        return b

    for i in range(dg.__len__()):
        find.append(*Linear(['Journey Distance(m)', 'Uber Type'], ['Fare$'], i))

    find = list(find)
    k = 0
    m = 0
    fare = list()
    for i in range(l.__len__()):
        if l[i]:
            fare.append(find[k])
            k += 1
        else:
            fare.append(e[m])
            m += 1
    df.drop('Fare$', axis=1)
    df['Fare$'] = fare
    print(df)
    df.to_csv('missing_values_solution.csv')

misingvalues()