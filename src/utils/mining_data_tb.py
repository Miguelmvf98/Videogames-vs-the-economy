import pandas as pd
import numpy as np
import numbers


# Function that has all the information from gdp_per_capita.ipynb
def all_gdp_per_capita():
    """Could not use a normal separation when creating the dataframe and so used error_bad_lines=False which forced the info to fit the dataframe"""
    gdp_per_capita = pd.read_csv("../data/gdp.csv", error_bad_lines=False)

    """Removed all nan values"""
    gdp_per_capita=gdp_per_capita.dropna(axis=1, how='all')

    """Made a list with all the countries that I wanted (all EU countries) and used it to remove the rest from my dataframe"""
    eu_countries=["Austria", "Belgium", "Bulgaria", "Croatia", "Republic of Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden", "United Kingdom", "Euro area"]
    gdp_per_capita_1 = gdp_per_capita[gdp_per_capita["Country "].isin(eu_countries)]

    """Made the dataframe in alphabetical order"""
    gdp_per_capita = gdp_per_capita_1.sort_values('Country ', ascending=True)
    gdp_per_capita = gdp_per_capita.set_index("Country ")

    """Took care of the NaN values"""
    gdp_per_capita = gdp_per_capita.dropna()

    """Renamed "Country Code" column to "geo" and set it as index"""
    gdp_per_capita= gdp_per_capita.rename(columns={"Country Code": "geo"})
    gdp_per_capita = gdp_per_capita.set_index("geo")

    """Started to create plots and saved them in functions"""
    emu_gdp_df = gdp_per_capita.loc["EMU"]
    esp_gdp_df = gdp_per_capita.loc["ESP"]
    deu_gdp_df = gdp_per_capita.loc["DEU"]
    fra_gdp_df = gdp_per_capita.loc["FRA"]
    gbr_gdp_df = gdp_per_capita.loc["GBR"]
    prt_gdp_df = gdp_per_capita.loc["PRT"]
    
    return emu_gdp_df, esp_gdp_df, deu_gdp_df, fra_gdp_df, gbr_gdp_df, prt_gdp_df


#Function that shows the work from inflation_rates.ipynb
def all_inflation_rates():
    """Made a dataframe from a csv downloaded into a local file"""
    eu_inflation_rates = pd.read_csv("../data/eu_inflation_rates.csv", sep= "\s" )

    """Removed columns containing nan values"""
    eu_inflation_rates=eu_inflation_rates.dropna(axis=1, how='all')

    """Changed the name of the column geo"""
    eu_inflation_rates= eu_inflation_rates.rename(columns={",geo\TIME_PERIOD": "geo"})

    """Used RegEx to remove the unwanted information from the column geo"""
    eu_inflation_rates['geo'] = eu_inflation_rates['geo'].str.replace(r'[^A-Z]', '')

    """Removed certain rows that I didnt need"""
    eu_inflation_rates = eu_inflation_rates.drop([eu_inflation_rates.index[9] ,eu_inflation_rates.index[10], eu_inflation_rates.index[15], eu_inflation_rates.index[16]])

    """Set the column geo as the index"""
    eu_inflation_rates= eu_inflation_rates.set_index("geo")

    """Started to create plots and saved them in functions"""
    eu_ir_df = eu_inflation_rates.loc["EU"]
    es_ir_df = eu_inflation_rates.loc["ES"]
    de_ir_df = eu_inflation_rates.loc["DE"]
    fr_ir_df = eu_inflation_rates.loc["FR"]
    uk_ir_df = eu_inflation_rates.loc["UK"]
    pt_ir_df = eu_inflation_rates.loc["PT"]

    return eu_ir_df, es_ir_df, de_ir_df, fr_ir_df, uk_ir_df, pt_ir_df


#Function that shows the work from unemployment.ipynb
def unemployment():
    """Imported the file and made it into a dataframe"""
    eu_unemployment_rates = pd.read_csv("../data/EU_unemployment_rates.tsv", sep= "," )

    """Removed the sex column"""
    eu_unemployment_rates.drop("sex", inplace=True, axis=1)

    """Removed three more columns"""
    eu_unemployment_rates.drop("s_adj", inplace=True, axis=1)
    eu_unemployment_rates.drop("age", inplace=True, axis=1)
    eu_unemployment_rates.drop("unit", inplace=True, axis=1)

    """Made the dataframe into a csv in order to be able to separate with a space and make a new dataframe more eligible"""
    eu_unemployment_rates.to_csv("eu_unemployment_rates_1.csv")

    """Imported the new csv and applied the appropiate separation"""
    eu_unemployment_rates_1 = pd.read_csv("../data/eu_unemployment_rates_1.csv", sep= "\t")

    """Changed the name of a column to geo"""
    eu_unemployment_rates_1= eu_unemployment_rates_1.rename(columns={",geo\\time": 'geo'})

    """Using RegEx I erased from the column geo all the info I didnt need"""
    eu_unemployment_rates_1['geo'] = eu_unemployment_rates_1['geo'].str.replace(r'[^A-Z]', '')

    """Removed the month from all the columns, leaving it with only the year"""
    eu_unemployment_rates_1=eu_unemployment_rates_1.rename(columns = lambda x : str(x)[:-4])
    eu_unemployment_rates_1= eu_unemployment_rates_1.rename(columns={"ge": 'geo'})

    """Used lamda to make a function that produced the mean from the columns with the same year"""
    eu_unemployment_rates_1=eu_unemployment_rates_1.groupby(by=eu_unemployment_rates_1.columns, axis=1).apply(lambda g: g.mean(axis=1) if isinstance(g.iloc[0,0], numbers.Number) else g.iloc[:,0])
    eu_unemployment_rates_2 = eu_unemployment_rates_1.iloc[:40]

    """gave a name to the geo column"""
    eu_unemployment_rates_2 = eu_unemployment_rates_2.rename(columns={"": "geo"})

    """Removed the rows that werent useful"""
    eu_unemployment_rates_2 = eu_unemployment_rates_2.drop([eu_unemployment_rates_2.index[9], eu_unemployment_rates_2.index[10], eu_unemployment_rates_2.index[14], eu_unemployment_rates_2.index[15], eu_unemployment_rates_2.index[17]])

    """Made the column geo into an index"""
    eu_unemployment_rates_2= eu_unemployment_rates_2.set_index("geo")

    """Turned all ":" values into NaN"""
    eu_unemployment_rates_2.replace(to_replace = ": ", value = 0, inplace = True)

    """Removed all non-numeric values from the dataframe"""
    for x in eu_unemployment_rates_2.columns:
        eu_unemployment_rates_2[x]=eu_unemployment_rates_2[x].str.extract('(\d+)', expand=False)

    """Attempted to remove spaces from the values"""
    eu_unemployment_rates_2["1983"] = eu_unemployment_rates_2["1983"].str.rstrip()
    eu_unemployment_rates_2["1984"] = eu_unemployment_rates_2["1984"].str.rstrip()
    eu_unemployment_rates_2["1985"] = eu_unemployment_rates_2["1985"].str.rstrip()
    eu_unemployment_rates_2["1986"] = eu_unemployment_rates_2["1986"].str.rstrip()
    eu_unemployment_rates_2["1987"] = eu_unemployment_rates_2["1987"].str.rstrip()
    eu_unemployment_rates_2["1988"] = eu_unemployment_rates_2["1988"].str.rstrip()
    eu_unemployment_rates_2["1989"] = eu_unemployment_rates_2["1989"].str.rstrip()
    eu_unemployment_rates_2["1990"] = eu_unemployment_rates_2["1990"].str.rstrip()
    eu_unemployment_rates_2["1991"] = eu_unemployment_rates_2["1991"].str.rstrip()
    eu_unemployment_rates_2["1992"] = eu_unemployment_rates_2["1992"].str.rstrip()
    eu_unemployment_rates_2["1993"] = eu_unemployment_rates_2["1993"].str.rstrip()
    eu_unemployment_rates_2["1994"] = eu_unemployment_rates_2["1994"].str.rstrip()
    eu_unemployment_rates_2["1995"] = eu_unemployment_rates_2["1995"].str.rstrip()
    eu_unemployment_rates_2["1996"] = eu_unemployment_rates_2["1996"].str.rstrip()
    eu_unemployment_rates_2["1997"] = eu_unemployment_rates_2["1997"].str.rstrip()
    eu_unemployment_rates_2["1998"] = eu_unemployment_rates_2["1998"].str.rstrip()
    eu_unemployment_rates_2["1999"] = eu_unemployment_rates_2["1999"].str.rstrip()
    eu_unemployment_rates_2["2000"] = eu_unemployment_rates_2["2000"].str.rstrip()
    eu_unemployment_rates_2["2001"] = eu_unemployment_rates_2["2001"].str.rstrip()
    eu_unemployment_rates_2["2002"] = eu_unemployment_rates_2["2002"].str.rstrip()
    eu_unemployment_rates_2["2003"] = eu_unemployment_rates_2["2003"].str.rstrip()
    eu_unemployment_rates_2["2004"] = eu_unemployment_rates_2["2004"].str.rstrip()
    eu_unemployment_rates_2["2005"] = eu_unemployment_rates_2["2005"].str.rstrip()
    eu_unemployment_rates_2["2006"] = eu_unemployment_rates_2["2006"].str.rstrip()
    eu_unemployment_rates_2["2007"] = eu_unemployment_rates_2["2007"].str.rstrip()
    eu_unemployment_rates_2["2008"] = eu_unemployment_rates_2["2008"].str.rstrip()
    eu_unemployment_rates_2["2009"] = eu_unemployment_rates_2["2009"].str.rstrip()
    eu_unemployment_rates_2["2010"] = eu_unemployment_rates_2["2010"].str.rstrip()
    eu_unemployment_rates_2["2011"] = eu_unemployment_rates_2["2011"].str.rstrip()
    eu_unemployment_rates_2["2012"] = eu_unemployment_rates_2["2012"].str.rstrip()
    eu_unemployment_rates_2["2013"] = eu_unemployment_rates_2["2013"].str.rstrip()
    eu_unemployment_rates_2["2014"] = eu_unemployment_rates_2["2014"].str.rstrip()
    eu_unemployment_rates_2["2015"] = eu_unemployment_rates_2["2015"].str.rstrip()
    eu_unemployment_rates_2["2016"] = eu_unemployment_rates_2["2016"].str.rstrip()
    eu_unemployment_rates_2["2017"] = eu_unemployment_rates_2["2017"].str.rstrip()
    eu_unemployment_rates_2["2018"] = eu_unemployment_rates_2["2018"].str.rstrip()
    eu_unemployment_rates_2["2019"] = eu_unemployment_rates_2["2019"].str.rstrip()
    eu_unemployment_rates_2["2020"] = eu_unemployment_rates_2["2020"].str.rstrip()

    """Turned all values into floats or ints"""
    eu_unemployment_rates_2= eu_unemployment_rates_2.apply(pd.to_numeric)

    """Filled all nan values with the average of each row"""
    eu_unemployment_rates= eu_unemployment_rates_2.apply(lambda x: x.fillna(x.mean()),axis=1)

    """Started to create plots and saved them in functions"""
    eu_ur_df = eu_unemployment_rates.loc["EU"]
    es_ur_df = eu_unemployment_rates.loc["ES"]
    de_ur_df = eu_unemployment_rates.loc["DE"]
    fr_ur_df = eu_unemployment_rates.loc["FR"]
    uk_ur_df = eu_unemployment_rates.loc["UK"]
    pt_ur_df = eu_unemployment_rates.loc["PT"]

    return eu_ur_df, es_ur_df, de_ur_df, fr_ur_df, uk_ur_df, pt_ur_df

#In order to plot unemployment rates and inflation rates it was necesary to create a new function, nearly identical to the unemployment one, with minor changes at the bottom and a different return
def unemployment_2008_2019():
    """Imported the file and made it into a dataframe"""
    eu_unemployment_rates = pd.read_csv("../data/EU_unemployment_rates.tsv", sep= "," )

    """Removed the sex column"""
    eu_unemployment_rates.drop("sex", inplace=True, axis=1)

    """Removed three more columns"""
    eu_unemployment_rates.drop("s_adj", inplace=True, axis=1)
    eu_unemployment_rates.drop("age", inplace=True, axis=1)
    eu_unemployment_rates.drop("unit", inplace=True, axis=1)

    """Made the dataframe into a csv in order to be able to separate with a space and make a new dataframe more eligible"""
    eu_unemployment_rates.to_csv("eu_unemployment_rates_1.csv")

    """Imported the new csv and applied the appropiate separation"""
    eu_unemployment_rates_1 = pd.read_csv("../data/eu_unemployment_rates_1.csv", sep= "\t")

    """Changed the name of a column to geo"""
    eu_unemployment_rates_1= eu_unemployment_rates_1.rename(columns={",geo\\time": 'geo'})

    """Using RegEx I erased from the column geo all the info I didnt need"""
    eu_unemployment_rates_1['geo'] = eu_unemployment_rates_1['geo'].str.replace(r'[^A-Z]', '')

    """Removed the month from all the columns, leaving it with only the year"""
    eu_unemployment_rates_1=eu_unemployment_rates_1.rename(columns = lambda x : str(x)[:-4])
    eu_unemployment_rates_1= eu_unemployment_rates_1.rename(columns={"ge": 'geo'})

    """Used lamda to make a function that produced the mean from the columns with the same year"""
    eu_unemployment_rates_1=eu_unemployment_rates_1.groupby(by=eu_unemployment_rates_1.columns, axis=1).apply(lambda g: g.mean(axis=1) if isinstance(g.iloc[0,0], numbers.Number) else g.iloc[:,0])
    eu_unemployment_rates_2 = eu_unemployment_rates_1.iloc[:40]

    """gave a name to the geo column"""
    eu_unemployment_rates_2 = eu_unemployment_rates_2.rename(columns={"": "geo"})

    """Removed the rows that werent useful"""
    eu_unemployment_rates_2 = eu_unemployment_rates_2.drop([eu_unemployment_rates_2.index[9], eu_unemployment_rates_2.index[10], eu_unemployment_rates_2.index[14], eu_unemployment_rates_2.index[15], eu_unemployment_rates_2.index[17]])

    """Made the column geo into an index"""
    eu_unemployment_rates_2= eu_unemployment_rates_2.set_index("geo")

    """Turned all ":" values into NaN"""
    eu_unemployment_rates_2.replace(to_replace = ": ", value = 0, inplace = True)

    """Removed all non-numeric values from the dataframe"""
    for x in eu_unemployment_rates_2.columns:
        eu_unemployment_rates_2[x]=eu_unemployment_rates_2[x].str.extract('(\d+)', expand=False)

    """Attempted to remove spaces from the values"""
    eu_unemployment_rates_2["1983"] = eu_unemployment_rates_2["1983"].str.rstrip()
    eu_unemployment_rates_2["1984"] = eu_unemployment_rates_2["1984"].str.rstrip()
    eu_unemployment_rates_2["1985"] = eu_unemployment_rates_2["1985"].str.rstrip()
    eu_unemployment_rates_2["1986"] = eu_unemployment_rates_2["1986"].str.rstrip()
    eu_unemployment_rates_2["1987"] = eu_unemployment_rates_2["1987"].str.rstrip()
    eu_unemployment_rates_2["1988"] = eu_unemployment_rates_2["1988"].str.rstrip()
    eu_unemployment_rates_2["1989"] = eu_unemployment_rates_2["1989"].str.rstrip()
    eu_unemployment_rates_2["1990"] = eu_unemployment_rates_2["1990"].str.rstrip()
    eu_unemployment_rates_2["1991"] = eu_unemployment_rates_2["1991"].str.rstrip()
    eu_unemployment_rates_2["1992"] = eu_unemployment_rates_2["1992"].str.rstrip()
    eu_unemployment_rates_2["1993"] = eu_unemployment_rates_2["1993"].str.rstrip()
    eu_unemployment_rates_2["1994"] = eu_unemployment_rates_2["1994"].str.rstrip()
    eu_unemployment_rates_2["1995"] = eu_unemployment_rates_2["1995"].str.rstrip()
    eu_unemployment_rates_2["1996"] = eu_unemployment_rates_2["1996"].str.rstrip()
    eu_unemployment_rates_2["1997"] = eu_unemployment_rates_2["1997"].str.rstrip()
    eu_unemployment_rates_2["1998"] = eu_unemployment_rates_2["1998"].str.rstrip()
    eu_unemployment_rates_2["1999"] = eu_unemployment_rates_2["1999"].str.rstrip()
    eu_unemployment_rates_2["2000"] = eu_unemployment_rates_2["2000"].str.rstrip()
    eu_unemployment_rates_2["2001"] = eu_unemployment_rates_2["2001"].str.rstrip()
    eu_unemployment_rates_2["2002"] = eu_unemployment_rates_2["2002"].str.rstrip()
    eu_unemployment_rates_2["2003"] = eu_unemployment_rates_2["2003"].str.rstrip()
    eu_unemployment_rates_2["2004"] = eu_unemployment_rates_2["2004"].str.rstrip()
    eu_unemployment_rates_2["2005"] = eu_unemployment_rates_2["2005"].str.rstrip()
    eu_unemployment_rates_2["2006"] = eu_unemployment_rates_2["2006"].str.rstrip()
    eu_unemployment_rates_2["2007"] = eu_unemployment_rates_2["2007"].str.rstrip()
    eu_unemployment_rates_2["2008"] = eu_unemployment_rates_2["2008"].str.rstrip()
    eu_unemployment_rates_2["2009"] = eu_unemployment_rates_2["2009"].str.rstrip()
    eu_unemployment_rates_2["2010"] = eu_unemployment_rates_2["2010"].str.rstrip()
    eu_unemployment_rates_2["2011"] = eu_unemployment_rates_2["2011"].str.rstrip()
    eu_unemployment_rates_2["2012"] = eu_unemployment_rates_2["2012"].str.rstrip()
    eu_unemployment_rates_2["2013"] = eu_unemployment_rates_2["2013"].str.rstrip()
    eu_unemployment_rates_2["2014"] = eu_unemployment_rates_2["2014"].str.rstrip()
    eu_unemployment_rates_2["2015"] = eu_unemployment_rates_2["2015"].str.rstrip()
    eu_unemployment_rates_2["2016"] = eu_unemployment_rates_2["2016"].str.rstrip()
    eu_unemployment_rates_2["2017"] = eu_unemployment_rates_2["2017"].str.rstrip()
    eu_unemployment_rates_2["2018"] = eu_unemployment_rates_2["2018"].str.rstrip()
    eu_unemployment_rates_2["2019"] = eu_unemployment_rates_2["2019"].str.rstrip()
    eu_unemployment_rates_2["2020"] = eu_unemployment_rates_2["2020"].str.rstrip()

    """Turned all values into floats or ints"""
    eu_unemployment_rates_2= eu_unemployment_rates_2.apply(pd.to_numeric)

    """Filled all nan values with the average of each row"""
    eu_unemployment_rates= eu_unemployment_rates_2.apply(lambda x: x.fillna(x.mean()),axis=1)

    """Sliced the dataframe to give me only the data from the year 2008 to 2019"""
    eu_unemployment_rates_2008_2019= eu_unemployment_rates.loc[:,"2008":'2019']

    eu_ur_df_2008_2019 = eu_unemployment_rates_2008_2019.loc["EU"]

    return eu_ur_df_2008_2019





#Function that shows the work from videogame_sales.ipynb
def all_videogames():
    """Imported the csv file and turned it into a dataframe"""
    videogame_sales = pd.read_csv("../data/videogamesales.csv", sep= "," )

    """Removed the unwanted columns"""
    videogame_sales.drop('JP_Sales', inplace=True, axis=1)
    videogame_sales.drop('Other_Sales', inplace=True, axis=1)
    videogame_sales.drop('Genre', inplace=True, axis=1)
    videogame_sales.drop('Rank', inplace=True, axis=1)
    videogame_sales.drop('NA_Sales', inplace=True, axis=1)
    videogame_sales.drop('Publisher', inplace=True, axis=1)

    """Searched for the nan values and removed them"""
    videogame_sales.sort_values(by=['Year'], inplace=True)
    videogame_sales.dropna(subset = ["Year"], inplace=True)

    """Grouped the data after choosing the column "Platform" """
    videogame_sales.sort_values(by=['Platform'], inplace=True)

    """Once I figured out which column I wanted (Platform), I checked the names of the different entrances"""
    videogame_sales["Platform"].unique()

    """Made 3 lists which contained the 3 most recognisable gaming consoles, and left out the unwanted data"""
    x_box1 = ['XB', 'X360', "XOne"]
    play_station1 = ["PS", 'PS2', 'PS3', "PS4", "PSP", "PSV"]
    nintendo1 = ["NES", "SNES", "N64", "GBA", "GB", "Wii", "WiiU", "DS", "3DS"]

    """XBox"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    x_box_sales = videogame_sales[videogame_sales['Platform'].apply(lambda x: any([y in x for y in x_box1]))]
    """Then sorted the data in ascending order by Year"""
    x_box_sales=x_box_sales.sort_values("Year", ascending=True)
    """Started to create plots"""
    eu_x_box_sales= x_box_sales.groupby('Year')['EU_Sales'].sum() 

    """PlayStation"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    play_station_sales = videogame_sales[videogame_sales['Platform'].apply(lambda x: any([y in x for y in play_station1]))]
    """Then sorted the data in ascending order by Year"""
    play_station_sales=play_station_sales.sort_values("Year", ascending=True)
    """Started to create plots"""
    eu_play_station_sales=play_station_sales.groupby('Year')['EU_Sales'].sum()

    """Nintendo"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    nintendo_sales = videogame_sales[videogame_sales['Platform'].apply(lambda x: any([y in x for y in nintendo1]))]
    """Then sorted the data in ascending order by Year"""
    nintendo_sales= nintendo_sales.sort_values("Year", ascending=True)
    """Started to create plots"""
    eu_nintendo_sales=nintendo_sales.groupby('Year')['EU_Sales'].sum() 

    return eu_x_box_sales, eu_play_station_sales, eu_nintendo_sales

#In order to make a new plot with sliced data a similar function was used
def all_videogames_2008_2017():
    """Imported the csv file and turned it into a dataframe"""
    videogame_sales = pd.read_csv("../data/videogamesales.csv", sep= "," )

    """Removed the unwanted columns"""
    videogame_sales.drop('JP_Sales', inplace=True, axis=1)
    videogame_sales.drop('Other_Sales', inplace=True, axis=1)
    videogame_sales.drop('Genre', inplace=True, axis=1)
    videogame_sales.drop('Rank', inplace=True, axis=1)
    videogame_sales.drop('NA_Sales', inplace=True, axis=1)
    videogame_sales.drop('Publisher', inplace=True, axis=1)

    """Searched for the nan values and removed them"""
    videogame_sales.sort_values(by=['Year'], inplace=True)
    videogame_sales.dropna(subset = ["Year"], inplace=True)

    """Grouped the data after choosing the column "Platform" """
    videogame_sales.sort_values(by=['Platform'], inplace=True)

    """Once I figured out which column I wanted (Platform), I checked the names of the different entrances"""
    videogame_sales["Platform"].unique()

    """Made 3 lists which contained the 3 most recognisable gaming consoles, and left out the unwanted data"""
    x_box1 = ['XB', 'X360', "XOne"]
    play_station1 = ["PS", 'PS2', 'PS3', "PS4", "PSP", "PSV"]
    nintendo1 = ["NES", "SNES", "N64", "GBA", "GB", "Wii", "WiiU", "DS", "3DS"]

    """Made the dataframe smaller by only selecting the years 2008-2017"""
    videogame_sales_2008_2017=videogame_sales.sort_values("Year", ascending=True)
    videogame_sales_2008_2017=videogame_sales_2008_2017.set_index("Year")
    videogame_sales_2008_2017=videogame_sales_2008_2017.loc[2008.0:2017.0]

    """XBox"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    x_box_sales = videogame_sales_2008_2017[videogame_sales_2008_2017['Platform'].apply(lambda x: any([y in x for y in x_box1]))]
    """Then sorted the data in ascending order by Year"""
    x_box_sales=x_box_sales.sort_values("Year", ascending=True)
    """Started to create plots"""
    eu_x_box_sales= x_box_sales.groupby('Year')['EU_Sales'].sum() 

    """PlayStation"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    play_station_sales = videogame_sales_2008_2017[videogame_sales_2008_2017['Platform'].apply(lambda x: any([y in x for y in play_station1]))]
    """Then sorted the data in ascending order by Year"""
    play_station_sales=play_station_sales.sort_values("Year", ascending=True)
    """Started to create plots"""
    eu_play_station_sales=play_station_sales.groupby('Year')['EU_Sales'].sum()

    """Nintendo"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    nintendo_sales = videogame_sales_2008_2017[videogame_sales_2008_2017['Platform'].apply(lambda x: any([y in x for y in nintendo1]))]
    """Then sorted the data in ascending order by Year"""
    nintendo_sales= nintendo_sales.sort_values("Year", ascending=True)
    """Started to create plots"""
    eu_nintendo_sales=nintendo_sales.groupby('Year')['EU_Sales'].sum() 

    return eu_x_box_sales, eu_play_station_sales, eu_nintendo_sales


#In order to make the correlation matrix for nintendo I needed to vary the main function and have different return
def nintendo_correlation_matrix():
    """Imported the csv file and turned it into a dataframe"""
    videogame_sales = pd.read_csv("../data/videogamesales.csv", sep= "," )

    """Removed the unwanted columns"""
    videogame_sales.drop('JP_Sales', inplace=True, axis=1)
    videogame_sales.drop('Other_Sales', inplace=True, axis=1)
    videogame_sales.drop('Genre', inplace=True, axis=1)
    videogame_sales.drop('Rank', inplace=True, axis=1)
    videogame_sales.drop('NA_Sales', inplace=True, axis=1)
    videogame_sales.drop('Publisher', inplace=True, axis=1)

    """Searched for the nan values and removed them"""
    videogame_sales.sort_values(by=['Year'], inplace=True)
    videogame_sales.dropna(subset = ["Year"], inplace=True)

    """Grouped the data after choosing the column "Platform" """
    videogame_sales.sort_values(by=['Platform'], inplace=True)

    """Once I figured out which column I wanted (Platform), I checked the names of the different entrances"""
    videogame_sales["Platform"].unique()

    """Made 1 list which contained nintendo gaming consoles, and left out the unwanted data"""
    nintendo1 = ["NES", "SNES", "N64", "GBA", "GB", "Wii", "WiiU", "DS", "3DS"]

    """Nintendo"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    nintendo_sales = videogame_sales[videogame_sales['Platform'].apply(lambda x: any([y in x for y in nintendo1]))]
    """Then sorted the data in ascending order by Year"""
    nintendo_sales= nintendo_sales.sort_values("Year", ascending=True)

    return nintendo_sales


#In order to show the marketshare in a piechart a new function was needed, very similar to all_videogames(), with a slight change at the end and different return
def all_videogames_pc():
    """Imported the csv file and turned it into a dataframe"""
    videogame_sales = pd.read_csv("../data/videogamesales.csv", sep= "," )

    """Removed the unwanted columns"""
    videogame_sales.drop('JP_Sales', inplace=True, axis=1)
    videogame_sales.drop('Other_Sales', inplace=True, axis=1)
    videogame_sales.drop('Genre', inplace=True, axis=1)
    videogame_sales.drop('Rank', inplace=True, axis=1)
    videogame_sales.drop('NA_Sales', inplace=True, axis=1)
    videogame_sales.drop('Publisher', inplace=True, axis=1)

    """Searched for the nan values and removed them"""
    videogame_sales.sort_values(by=['Year'], inplace=True)
    videogame_sales.dropna(subset = ["Year"], inplace=True)

    """Grouped the data after choosing the column "Platform" """
    videogame_sales.sort_values(by=['Platform'], inplace=True)

    """Once I figured out which column I wanted (Platform), I checked the names of the different entrances"""
    videogame_sales["Platform"].unique()

    """Made 3 lists which contained the 3 most recognisable gaming consoles, and left out the unwanted data"""
    x_box1 = ['XB', 'X360', "XOne"]
    play_station1 = ["PS", 'PS2', 'PS3', "PS4", "PSP", "PSV"]
    nintendo1 = ["NES", "SNES", "N64", "GBA", "GB", "Wii", "WiiU", "DS", "3DS"]

    """XBox"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    x_box_sales = videogame_sales[videogame_sales['Platform'].apply(lambda x: any([y in x for y in x_box1]))]

    """PlayStation"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    play_station_sales = videogame_sales[videogame_sales['Platform'].apply(lambda x: any([y in x for y in play_station1]))]

    """Nintendo"""
    """Used the lists to make a function that gave me 3 different dataframes with the information of the consoles I wanted"""
    nintendo_sales = videogame_sales[videogame_sales['Platform'].apply(lambda x: any([y in x for y in nintendo1]))]

    """In order to make the piechart it was necessary to find out how many videogames each of the 3 consoles sold in the eu"""
    sum_nintendo_sales_eu=nintendo_sales["EU_Sales"].sum()
    sum_play_station_sales_eu=play_station_sales["EU_Sales"].sum()
    sum_x_box_sales_eu=x_box_sales["EU_Sales"].sum()

    """Then divide by the total to find the percentage"""
    total_sum = sum_nintendo_sales_eu + sum_play_station_sales_eu + sum_x_box_sales_eu
    nintendo_percentage= sum_nintendo_sales_eu/total_sum
    play_station_percentage= sum_play_station_sales_eu/total_sum
    x_box_percentage= sum_x_box_sales_eu/total_sum

    return nintendo_percentage, play_station_percentage, x_box_percentage