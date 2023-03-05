#Imporing Matplotlib to draw the plot and pandas to fetch files
import matplotlib.pyplot as plt
import pandas as pd

def piechart():
    """
        this function reads the Data of different types of population
        in United Kingdom in 2021
    """
    
    #Importing Population data of 2021 living in UK
    df = pd.read_csv('population.csv')

    #Get percentage of population (Value) column and required fields
    x=df['Value']

    #Get labels (Ethnicity) column and required fields
    y=df['Ethnicity']
    
    #Selecting the rows we need for our Pie chart
    x1=x[1:6]
    y1=y[1:6] 
        
    #figure size
    plt.figure(figsize=(5, 5))

    #plot the Pie chart
    plt.pie(x1, labels = y1, autopct='%1.1f%%', startangle=90)
    
    #Title of the line chart
    plt.title("2021 Population data of communities living in UK")

    #Show Legends to identify which colour belongs to which population
    plt.legend()

    #show plot
    plt.show()
        
piechart()