**NOTICE**: the data includes \* -characters that represent NoData values.

The most important attributes for this exercise are:

 - **USAF** = the station ID number
   - 028450 : Rovaniemi
   - 029980 : Helsinki Kumpula
 - **YR--MODAHRMN** = Year-Month-Day-Hour-Minute in Greenwich Mean Time (GMT)
 - **TEMP** = Temperature in Fahrenheit
 - **MAX** = Maximum temperature in Fahrenheit
 - **MIN** = Minimum temperature in Fahrenheit

## Problem 1 - Basic statistics of the data

In this problem your task is to  explore the data from [6153237444115dat.csv](6153237444115dat.csv) by reading the data into Pandas
and conduct following tasks / answer to following questions:

- Read the data into a variable called `data`.
  - **Important**: When reading the data, it is important that you tell to Pandas that no-data values are specified with varying number of \* characters.
  - You can do this by specifying a following parameter in the `read_csv()` -function:
     - `na_values=['*', '**', '***', '****', '*****', '******']`
- How many rows is there in the data?
- What are the column names?
- What are the datatypes of the columns?
- What is the mean Fahrenheit temperature in the data? (`TEMP` column)
- What is the standard deviation of the Maximum temperature? (`MAX` column)
- How many unique stations exists in the data? (`USAF` column)

You should write your codes into a `data_exploration.py` file and print the answers for the questions above
inside the script.

## Problem 2 - Data manipulation

Similarly as in earlier exercises the temperatures in our data are represented in Fahrenheit, hence,
you need to convert the temperatures into Celsius.

 - Select from the `data` columns `USAF, YR--MODAHRMN, TEMP, MAX, MIN` and assign them into a new variable called `selected`
 - Remove all rows from `selected` that has NoData in column `TEMP` using `dropna()` -function
 - Convert the Fahrenheit temperatures from `TEMP` into a new column `Celsius` using the conversion formula
 - Round the values in `Celsius` to have 0 decimals (**don't** create a new column --> update the current one)
 - Convert the `Celsius` values into integers (**don't** create a new column --> update the current one)

You can add your codes into a `data_exploration.py` file.

## Problem 3 - Data selection

In this problem you should divide the data into separate subsets for different stations and save those DataFrames into disk.

- Divide the selection into two separate datasets:
  - Select all rows from `selected` DataFrame into variable called `kumpula` where the `USAF` code is `29980`
  - Select all rows from `selected` DataFrame into variable called `rovaniemi` where the `USAF` code is `28450`
- Save `kumpula` DataFrame into `Kumpula_temps_May_Aug_2017.csv` file (CSV format) 
   - separate the columns with `,`
   - use only 2 decimals in the floating point numbers
- Save `rovaniemi` DataFrame into `Rovaniemi_temps_May_Aug_2017.csv` file (CSV format) 
   - separate the columns with `,`
   - use only 2 decimals in the floating point numbers

You can add your codes into a `data_exploration.py` file.

## Problem 4 - Data analysis

In this problem the aim is to understand how different the summer temperatures has been in Helsinki Kumpula and Rovaniemi.
Using the data from Problem 3 in `kumpula` and `rovaniemi` DataFrames answer to following questions:

**Part 1**

- What was the median temperature in:
  - Helsinki Kumpula?
  - Rovaniemi?

**Part 2**

Part 1 considers data from quite long period of time (May-Aug), hence the differences might not be so clear.
Let's find out what were the mean temperatures in May and June in Kumpula and Rovaniemi:

- Select from `rovaniemi` and `kumpula` DataFrames such rows from the DataFrames where ``YR--MODAHRMN`` values are from May 2017 (see hints for help)
and assign them into variables `rovaniemi_may` and `kumpula_may`
- Do similar procedure for June and assign those values into variables `rovaniemi_june` and `kumpula_june`
- Using those new subsets print the mean, min and max temperatures for both places in May and June.

You can add your codes into a `data_exploration.py` file.

Interpreting the results after the data analysis is one of the most important steps in a process called Knowledge Discovery.
Hence, use the information above to discuss shortly about following questions (justify your answers with the data analysis results):

- Does there seem to be large difference in temperatures between the months?
- Is Rovaniemi much colder place than Kumpula?



## Problem 5 (optional) - Parse daily temperatures

This optional task is for more advanced students (minimal guidance given).
Our current dataset contains hourly temperatures (actually 3 measurements per hour).

Your task here is to:

  - create a new DataFrame where you have calculated mean, max and min temperatures for each day separately using the
  hourly values from Rovaniemi and Helsinki Kumpula.
  - this problem is a classical data aggregation problem


