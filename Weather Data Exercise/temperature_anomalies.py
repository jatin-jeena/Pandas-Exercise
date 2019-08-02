import pandas as pd
data = pd.read_csv('anomalies.txt', sep ='\s+', na_values='-9999')
data = data.drop([0])
print(data)
count = 0
print(data['TAVG'].isna().sum())
print(23716 - len(data[data['TAVG'].isna()]))
print(23716 - len(data[data['TMIN'].isna()]))
print(data[0:1])
print(data[:-1])
print(data['TAVG'].astype(float).mean())
s = 0
j = 0
tem = data['TMAX'].values
for i in data['DATE']:
    j += 1
    if str(i)[2:6] == '6905' or str(i)[2:6] == '6906' or str(i)[2:6] == '6907' or str(i)[2:6] == '6908':
        s = max(s, float(tem[j]))
print(s)
df = data[['DATE', 'TAVG']]
df = df.dropna()
dl = df['DATE'].values
ml = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
ma = []
for i in range(dl.__len__()):
    dl[i] = dl[i][4:6]
df.TAVG = df.TAVG.astype(int)
for x, y in df.groupby('DATE'):
    ma.append(y['TAVG'].mean())
dma = pd.DataFrame({'maonth': ml, 'avgtemp': ma})
print(dma)
maf = list(dma.avgtemp)
dma.to_csv('monthlyData.csv')
for i in range(maf.__len__()):
    maf[i] = (maf[i] - 32)/1.8
dma['TempsC'] = maf
print(dma)
df = data[['DATE', 'TAVG']]
a = list(df.DATE)
for i in range(a.__len__()):
    a[i] = int(a[i][0:4])
df['DATEM'] = a
df = df[df['DATEM'] <= 1981]
df.DATE = df.DATE.astype(int)
df.DATE = df.DATE // 100
df.DATE = df.DATE % 100
m = []
df = df.drop('DATEM', axis = 1)
ma = []
df = df.dropna()
df.TAVG = df.TAVG.astype(int)
for x, y in df.groupby('DATE'):
    ma.append(y['TAVG'].mean())
dma = pd.DataFrame({'maonth': ml, 'avgtemp': ma})
maf = list(dma.avgtemp)
for i in range(maf.__len__()):
    maf[i] = (maf[i] - 32)/1.8
dma['TempsC'] = maf
dma.drop('avgtemp', axis = 1)
print(dma)
