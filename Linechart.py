#Imporing Matplotlib to draw the plot and pandas to fetch files
import matplotlib.pyplot as plt
import pandas as pd

def linechart():
    """
        this function reads the Data of average sale of four property 
        types in United Kingdom
    """
    #Average price by type of property in United Kingdom
    df = pd.read_csv('property-type-avg-united-kingdom.csv')
    
    #Creating variables for individual columns
    Date = df["Pivotable date"]
    Detached_hou = df["Average price Detached houses"]
    Sdetached_hou = df["Average price Semi-detached houses"]
    Terraced_hou = df["Average price Terraced houses"]
    Flats_maisonettes = df["Average price Flats and maisonettes"]

    #figure size
    plt.figure(figsize=(15, 5))

    #plot the line chart with ever country values in UK 
    plt.plot(Date, Detached_hou, label='Detached houses')
    plt.plot(Date, Sdetached_hou, label='Semi-detached houses')
    plt.plot(Date, Terraced_hou, label='Terraced houses')
    plt.plot(Date, Flats_maisonettes, label='Flats and maisonettes')

    #Title of the line chart
    plt.title("Average price by type of property in United Kingdom")

    #Title of the X label
    plt.xlabel("Months")

    #Title of the Y label
    plt.ylabel("Sale Price")

    #Show Legends to identify which colour belongs to which country
    plt.legend()

    #show plot
    plt.show()
    
linechart()