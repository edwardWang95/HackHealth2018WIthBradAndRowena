import folium
import pandas
from selenium import webdriver
import os
from selenium.common.exceptions import NoSuchElementException

reader = pandas.read_csv("city_of_new_york.csv")
map = None

def createMap():
    map = folium.Map(location=[40.7128, -74.0060],
                    zoom_start=12,
                    tiles='Stamen Terrain')
    absPath, filename = os.path.split(os.path.abspath(__file__))

    for i in range(100):
        x = reader["NUMBER"][i] + " " + reader["STREET"][i]
        color1 = webScrape(x, reader["POSTCODE"][i])
        folium.CircleMarker([reader["LAT"][i],reader["LON"][i]], radius = 5, popup=reader['STREET'][i], color = color1).add_to(map)

    map.save(absPath + '/map.html')

def webScrape(addr, zip):
    absPath, filename = os.path.split(os.path.abspath(__file__))
    browser = webdriver.Chrome(executable_path=absPath + '/chromedriver')
    url = 'https://datawarehouse.hrsa.gov/tools/analyzers/geo/ShortageArea.aspx'
    browser.get(url)
    address = browser.find_element_by_name("ctl00$ctl00$MainContent$ContentPlaceHolder1$tbxAddress")
    city = browser.find_element_by_name("ctl00$ctl00$MainContent$ContentPlaceHolder1$tbxCity")
    postalCode = browser.find_element_by_name("ctl00$ctl00$MainContent$ContentPlaceHolder1$tbxZIP")

    address.send_keys(str(addr))
    city.send_keys("New York")
    postalCode.send_keys(str(zip))
    browser.find_element_by_name("ctl00$ctl00$MainContent$ContentPlaceHolder1$lstState").send_keys("New York")
    browser.find_element_by_name("ctl00$ctl00$MainContent$ContentPlaceHolder1$btnDrill").click()
    try:
        a = browser.find_element_by_id("redesignDiv")
        a = str(a)
        if a.count("No") == 0:
            browser.close()
            return "#18ff01"
        elif a.count("No") == 1:
            browser.close()
            return "#ffff00"
        elif a.count("No") == 2:
            browser.close()
            return "#ffa200"
        elif a.count("No") == 3:
            browser.close()
            return "#ffa1b2"
        elif a.count("No") == 4:
            browser.close()
            return "#ff2600"
    except NoSuchElementException:
        browser.close()
        pass


createMap()