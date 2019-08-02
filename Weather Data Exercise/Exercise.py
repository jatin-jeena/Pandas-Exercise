import pandas as pd

# question 1

print("-"*10, "ONE", "-"*10)
df = pd.read_csv('Excercise.csv', na_values = ['*', '**', '***', '****', '*****', '******'])
print("Number of Rows :", df.__len__())
print("Columns :", *df.columns, sep = " , ")
print("Datatypes :")
print(df.dtypes)
print("Maximum temprature :", df['TEMP'].mean())
print("Standard Deviation :", df['MAX'].std())
print("Number of unique stations :",    df['USAF'].unique().__len__())

# question 2

print("-"*10, "TWO", "-"*10)
selected = pd.DataFrame({'USAF': list(df['USAF']), 'YR--MODAHRMN': list(df['YR--MODAHRMN']), 'TEMP': list(df['TEMP']), 'MAX': list(df['MAX']), 'MIN': list(df['MIN'])})
print(selected)
new = selected.dropna(axis=0, how="any", subset=['TEMP'])
print(new)
TEMP_C = []
for i in new["TEMP"]:
    TEMP_C.append((i-32)*5/9)
new['TEMP_C'] = TEMP_C
print(new)
new1 = []
print("temp", TEMP_C)
r = TEMP_C.__len__()
for i in range(r):
    new1.append(round(TEMP_C[i]))
print(new1)
new['TEMP_C'] = new1

# question 3

print("-"*10, "THREE", "-"*10)
kumpula = new[new['USAF'] == 29980]
rovaniemi = new[new['USAF'] == 28450]
df.to_csv('Kumpula_temps_May_Aug_2017.csv')
print(kumpula)
df.to_csv('Rovaniemi_temps_May_Aug_2017.csv')
print(rovaniemi)

# question 4

print("-"*10, "FOUR", "-"*10)
print()
print("-"*10, "PART_ONE", "-"*10)
ind = (kumpula.__len__()) / 2
print("Median temprature in Helsinki Kumpula :", list(kumpula['TEMP'])[int(ind)])
ind = (rovaniemi.__len__()+1) / 2
print("Median temprature in Helsinki Rovaniemi :", list(rovaniemi['TEMP'])[int(ind)])
print("-"*10, "PART_TWO", "-"*10)
kumpula_may = kumpula[kumpula['YR--MODAHRMN'] // 1000000 == 201705]
rovaniemi_may = rovaniemi[rovaniemi['YR--MODAHRMN'] // 1000000 == 201705]
print(kumpula_may)
print(rovaniemi_may)
kumpula_june = kumpula[kumpula['YR--MODAHRMN'] // 1000000 == 201706]
rovaniemi_june = rovaniemi[rovaniemi['YR--MODAHRMN'] // 1000000 == 201706]
print(kumpula_june)
print(rovaniemi_june)
print("Mean temprature of Kumpula in may:", kumpula_may['TEMP'].mean())
print("Mean temprature of Kumpula in june:", kumpula_may['TEMP'].mean())
print("Maximum temprature of Kumpula in may :", kumpula_may['TEMP'].max())
print("Maximum temprature of Kumpula in june :", kumpula_june['TEMP'].max())
print("Minimum temprature of Kumpula in may:", kumpula_may['TEMP'].min())
print("Minimum temprature of Kumpula in june:", kumpula_june['TEMP'].min())
print("Mean temprature of Rovaniemi in may:", rovaniemi_may['TEMP'].mean())
print("Mean temprature of Rovaniemi in june:", rovaniemi_june['TEMP'].mean())
print("Maximum temprature of Rovaniemi in may:", rovaniemi_may['TEMP'].max())
print("Maximum temprature of Rovaniemi in june:", rovaniemi_june['TEMP'].max())
print("Minimum temprature of Rovaniemi  in may:", rovaniemi_may['TEMP'].min())
print("Minimum temprature of Rovaniemi  in june:", rovaniemi_june['TEMP'].min())

print("Does there seem to be large difference in temperatures between the months?")
print("Yes, the difference between the tempratures is large \nIt is approximately ", kumpula_june['TEMP'].mean()- kumpula_may['TEMP'].mean(), " degress in Kumpula\n",rovaniemi_june['TEMP'].mean()- rovaniemi_may['TEMP'].mean(), "in Rovaniemi")
print("Is Rovaniemi much colder place than Kumpula?")
print("Yes, the average temprature of kumpula is ", kumpula['TEMP'].mean() - rovaniemi["TEMP"].mean(), " higher than rovaniemi")
print(df)
print(selected)
b = []
for i in selected['YR--MODAHRMN']:
    b.append(str(i)[0:10])
selected['hr'] = b
gb = selected.groupby('hr')
hmean = []
hmax = []
hmin = []
for x, y in gb:
    hmax.append(y['TEMP'].max())
    hmin.append(y['TEMP'].min())
    hmean.append(y['TEMP'].mean())
newdf = pd.DataFrame({'Mean':hmean, "Max":hmax, "Min":hmin})
newdf.to_csv("Result.csv")
print(newdf)












