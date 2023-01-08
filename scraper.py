from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)
page=requests.get(START_URL)

soup= bs(page.content, "html.parser")

star_table = soup.find_all('table')

list=[]

table_rows = star_table[7].find_all('tr')
# Webdriver


time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape_more_data(hyperlink):
    try:        

        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
          
            for td_tag in td_tags:
                try: 
                    list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    list.append("")
                    
        #planets_data.append(list)

    except:
        time.sleep(1)
        scrape_more_data(hyperlink)



def scrape():

    for i in range(0,10):
        
        print(f'Scrapping page {i+1} ...' )
        
        
        # BeautifulSoup Object     
        soup = bs(browser.page_source, "html.parser")

        # Loop to find element using XPATH
        for ul_tag in soup.find_all("ul", attrs={"class", "stars"}):

            li_tags = ul_tag.find_all("li")
           
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index != 0:                   
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)

        # Find all elements on the page and click to move to the next page
        
# Calling Method    
scrape()

# Define Header
headers = ["name", "distance", "mass", "radius"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
