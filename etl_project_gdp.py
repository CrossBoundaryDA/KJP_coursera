#import required libraries
import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import numpy as np

# def extract from HTML
def extract(url): #you will pass the url to bring in from the table
    html_content = requests.get(url).content #parse HTML from url
    data = BeautifulSoup(html_content, 'html.parser') #choose content to also bring in tags
    table = data.find_all('table')[2] #get content related to table at index 2
    count = 0
    #skip the first row and otherwise get all rows
    rows = table.find_all('tr')
    for row in rows:
        if count<5:
            col = row.find_all('td')
            if len(col)!=0: #remember to check number of cells in a row - many web tables have invisible merged rows
                data_dict = {"Country": col[1].contents[0],"GDP_USD": col[3].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
                count += 1 #final instruction increases count by one, which starts the loop over
            else:
                break
            return df

url = 'https://web.archive.org/web/20230902185326/https:/en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
df = extract(url)
print (df)