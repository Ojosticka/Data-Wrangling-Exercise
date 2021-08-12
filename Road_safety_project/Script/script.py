#Datopian - Data Wrangling Challenge (Script)


#Import the required libraries needed for this script
import pandas as pd

def get_data():
    '''
    Read the website with its url into the script
    Method - pd.read_html (reads all the tables in the website and puts them in a list)
    List indexing is used to get the required table
    '''

    df = pd.read_html('https://en.wikipedia.org/wiki/Road_safety_in_Europe')
    data = df[2]

    #Select the required columns from the table, filtering out the ones that won't be used 
    data = data[['Country', 'Area (thousands of km2)[24]', 'Population in 2018[25]', 'GDP per capita in 2018[26]', 'Population density (inhabitants per km2) in 2017[27]', 
             'Vehicle ownership (per thousand inhabitants) in 2016[28]', 'Total Road Deaths in 2018[30]', 'Road deaths per Million Inhabitants in 2018[30]']]

    #Rename the filtered columns to standard names as required.
    data = data.rename(columns={
        'Area (thousands of km2)[24]':'Area',
        'Population in 2018[25]':'Population',
        'GDP per capita in 2018[26]':'GDP per Capita',
        'Population density (inhabitants per km2) in 2017[27]':'Population Density',
        'Vehicle ownership (per thousand inhabitants) in 2016[28]':'Vehicle Ownership',
        'Total Road Deaths in 2018[30]':'Total Road Deaths',
        'Road deaths per Million Inhabitants in 2018[30]':'Road deaths per Million Inhabitants'}) 
    
    #Insert a Year column in the data and populate with a constant value of 2018
    data.insert(1, 'Year', 2018)

    #Sort data using the Road deaths per million inhabitants column, excluding the last row
    #The last row contains EU total for all countries, and should remain at the bottom of the table
    sorted_data = data[0:28].sort_values('Road deaths per Million Inhabitants')

    #Adding the EU total row back to the bottom of the sorted data.
    data = sorted_data.append(data.loc[28])

    #store the resulting dataset in a csv file, and filter out the index, allowing "Country" as first column in resulting csv file.
    data.to_csv('data.csv', index = False)

    return data

#call the function here
get_data()