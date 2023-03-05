import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def barchart():
    """
        this function reads the Data and compare the average price of
        three countries of uk
    """

    #Importing Sales values of UK from last five years
    #Comparison of average price of all property types for 3 locations
    df = pd.read_csv('Comparison-united-kingdom-scotland.csv')

    #Creating variables for individual columns
    Date = df["Date"]
    Eng = df["England"]
    Sco = df["Scotland"]
    Ire = df["Northern_Ireland"]

    X_axis = np.arange(len(Date))
    width = 0.2

    #figure size
    plt.figure(figsize=(15, 5))

    #plot the Bar chart with ever country values
    plt.bar(X_axis, Eng, 0.2, label='England')
    plt.bar(X_axis + width, Sco, 0.2, label='Scotland')
    plt.bar(X_axis + width*2, Ire, 0.2, label='Northern_Ireland')

    #Title of the Bar chart
    plt.title("Comparison of average price of property for 3 countries")

    #Title of the X label
    plt.xlabel("Monhts")

    #Title of the Y label
    plt.ylabel("Sale Prices")

    plt.xticks(X_axis + width, Date)

    #Show Legends to identify which colour belongs to which country
    plt.legend()
    
    #show plot
    plt.show()
    #plt.savefig('bar_chart.png')
    
barchart()