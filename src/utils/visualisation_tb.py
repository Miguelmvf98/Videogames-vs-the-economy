import matplotlib.pyplot as plt
import seaborn as sns

#Countries from EU gdp per capita graph
def all_eu_gdp_plot(var_1,var_2,var_3,var_4,var_5,var_6):
    plt.plot(var_1)
    plt.plot(var_2)
    plt.plot(var_3)
    plt.plot(var_4)
    plt.plot(var_5)
    plt.plot(var_6)
    plt.xticks(rotation='vertical')
    plt.legend(["EU", "Spain", "Germany", "France", "UK", "Portugal"])
    plt.xlabel("YEAR")
    plt.ylabel("GDP PER CAPITA ($)")
    plt.title("EU GDP PER CAPITA")
    
#Only EU gdp per capita graph
def eu_gdp_plot(var_1):
    plt.plot(var_1)
    plt.xticks(rotation='vertical')
    plt.legend(["EU"])
    plt.xlabel("YEAR")
    plt.ylabel("GDP PER CAPITA ($)")
    plt.title("EU GDP PER CAPITA")

#Only EU gdp per capita histogram
def histogram_gdp_eu(var_1):
    x = var_1 
    bins = 5
    plt.title('European GDP per capita 1990-2018',fontsize=20)
    plt.xlabel('GDP per capita ($)')
    plt.ylabel('Frequency',fontsize=10)
    plt.hist(x, bins, alpha=0.5, histtype='bar', ec='black')


#Countries from EU inflation rate graph
def all_eu_ir_plot(var_1,var_2,var_3,var_4,var_5,var_6):
    plt.plot(var_1)
    plt.plot(var_2)
    plt.plot(var_3)
    plt.plot(var_4)
    plt.plot(var_5)
    plt.plot(var_6)
    plt.xticks(rotation='vertical')
    plt.legend(["EU", "Spain", "Germany", "France", "UK", "Portugal"])
    plt.xlabel("YEAR")
    plt.ylabel("INFLATION RATE (%)")
    plt.title("EU INFLATION RATE")

# Only EU inflation rate graph
def eu_ir_plot(var_1):
    plt.plot(var_1)
    plt.xticks(rotation='vertical')
    plt.legend(["EU"])
    plt.xlabel("YEAR")
    plt.ylabel("INFLATION RATE (%)")
    plt.title("EU INFLATION RATE")

#Only EU inflation rate histogram
def histogram_ir_eu(var_1):
    x = var_1 
    bins = 5
    plt.title('European inflation rate 2008-2019',fontsize=20)
    plt.xlabel('Inflation rate (%)')
    plt.ylabel('Frequency',fontsize=10)
    plt.hist(x, bins, alpha=0.5, histtype='bar', ec='black')


#Countries from EU unemployment rate
def all_eu_unemployment_plot(var_1,var_2,var_3,var_4,var_5,var_6):
    plt.plot(var_1)
    plt.plot(var_2)
    plt.plot(var_3)
    plt.plot(var_4)
    plt.plot(var_5)
    plt.plot(var_6)
    plt.xticks(rotation='vertical')
    plt.xticks(fontsize=7)
    plt.legend(["EU", "Spain", "Germany", "France", "UK", "Portugal"])
    plt.xlabel("YEAR")
    plt.ylabel("UNEMPLOYMENT RATE (%)")
    plt.title("EU UNEMPLOYMNENT RATE")
    
#Only EU unemployment rate
def eu_unemployment_plot(var_1):
    plt.plot(var_1)
    plt.xticks(rotation='vertical')
    plt.xticks(fontsize=7)
    plt.legend(["EU"])
    plt.xlabel("YEAR")
    plt.ylabel("UNEMPLOYMENT RATE (%)")
    plt.title("EU UNEMPLOYMNENT RATE")

#Only EU unemployment rate: 2008-2019
def eu_unemployment_plot_2008_2019(var_1):
    plt.plot(var_1)
    plt.xticks(rotation='vertical')
    plt.xticks(fontsize=7)
    plt.legend(["EU"])
    plt.xlabel("YEAR")
    plt.ylabel("UNEMPLOYMENT RATE (%)")
    plt.title("EU UNEMPLOYMNENT RATE")

#Only EU unemployment rate histogram
def histogram_ur_eu(var_1):
    x = var_1
    bins = 5
    plt.title('European unemployment rate 1983-2020',fontsize=20)
    plt.xlabel('Unemployment rate (%)')
    plt.ylabel('Frequency',fontsize=10)
    plt.hist(x, bins, alpha=0.5, histtype='bar', ec='black')


# EU unemployment rate and EU inflation rate together
def ir_and_ur(var_1, var_2, var_3):
    """t= x axis, data1=eu unemployment rate, data2= eu inflation rate"""
    t = var_1
    data1 = var_2
    data2 = var_3

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Inflation Rate', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    """Make a second axes that shares the same x-axis"""
    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Unemployment Rate', color=color)
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title("INFLATION RATES VS UNEMPLOYMNENT RATE IN THE EU")
    """otherwise the right y-label is slightly clipped"""
    fig.tight_layout()


#Video game sales in the EU
def video_game_sales_eu(var_1, var_2, var_3):
    plt.plot(var_1)
    plt.plot(var_2)
    plt.plot(var_3)
    plt.xticks(rotation='vertical')
    plt.legend(["Nintendo", "Play Station", "Xbox"])
    plt.xlabel("YEAR")
    plt.ylabel("SALES (MILLIONS)")
    plt.title("VIDEOGAME SALES EU")

#Video game sales in the EU
def video_game_sales_eu_2008_2017(var_1, var_2, var_3):
    plt.plot(var_1)
    plt.plot(var_2)
    plt.plot(var_3)
    plt.xticks(rotation='vertical')
    plt.legend(["Nintendo", "Play Station", "Xbox"])
    plt.xlabel("YEAR")
    plt.ylabel("SALES (MILLIONS)")
    plt.title("VIDEOGAME SALES EU")


#Only Nintendo sales in EU
def nintendo_sales_eu(var_1):    
    plt.plot(var_1)
    plt.xticks(rotation='vertical')
    plt.legend(["Nintendo"])
    plt.xlabel("YEAR")
    plt.ylabel("SALES (MILLIONS)")
    plt.title("NINTENDO VIDEOGAME SALES EU")

#Histogram of video game sales from nintendo 1983-2020
def histogram_nintendo(var_1):    
    x = var_1
    bins = 5
    plt.title('Nintendo Video Game Sales 1983-2020',fontsize=20)
    plt.xlabel('Sales (millions)')
    plt.ylabel('Frequency',fontsize=10)
    plt.hist(x, bins, alpha=0.5, histtype='bar', ec='black')

#Correlation matrix (seaborn) Nintendo
def correlation_matrix_nintendo(var_1):
    corr = var_1.corr()
    ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(20, 220, n=200), square=True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.title('Correlation Matrix Nintendo', fontsize=16)

#Only PlayStation sales in EU
def play_station_sales_eu(var_1):    
    plt.plot(var_1)
    plt.xticks(rotation='vertical')
    plt.legend(["PlayStation"])
    plt.xlabel("YEAR")
    plt.ylabel("SALES (MILLIONS)")
    plt.title("PLAYSTATION VIDEOGAME SALES EU")

#Histogram of video game sales from play station 1994-2017
def histogram_play_station(var_1):
    x = var_1
    bins = 5
    plt.title('PlayStation Video Game Sales 1994-2017',fontsize=20)
    plt.xlabel('Sales (millions)')
    plt.ylabel('Frequency',fontsize=10)
    plt.hist(x, bins, alpha=0.5, histtype='bar', ec='black')

#Only Xbox sales in EU
def x_box_sales_eu(var_1):    
    plt.plot(var_1)
    plt.xticks(rotation='vertical')
    plt.legend(["Xbox"])
    plt.xlabel("YEAR")
    plt.ylabel("SALES (MILLIONS)")
    plt.title("XBOX VIDEOGAME SALES EU")

#Histogram of video game sales from xbox 2000-2016
def histogram_xbox(var_1):
    x = var_1
    bins = 5
    plt.title('Xbox Video Game Sales 2000-2016',fontsize=20)
    plt.xlabel('Sales (millions)')
    plt.ylabel('Frequency',fontsize=10)
    plt.hist(x, bins, alpha=0.5, histtype='bar', ec='black')

#Pie chart of video game marketshare of each console eu
def eu_console_marketshare(var_1, var_2, var_3):
    Consoles=["Nintendo", "PlayStation", "Xbox"] 
    Sales=[var_1*100, var_2*100, var_3*100]
    plt.pie(Sales, labels= Consoles,explode=(0.1, 0.1, 0.1), autopct='%1.2f%%')
    plt.title("Historic video game market share percentage of each console in the EU")
    

#Time consuming graph
def time_consuming():
    done=["Finding the Subject", "Finding Data", "Define Hypothesis", "Define Steps", "Cleaning Data, Making Graphs, Explaining Conclusion", "Document Steps"] 
    time=[5, 20, 10, 5, 50, 10]
    plt.pie(time, labels= done,explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1), autopct='%1.0f%%')
    plt.title("Aproximate Percentage of Time Invested \n in each Stage of the Project.")
    return plt.show()