from selenium import webdriver
import pandas
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re


file_path = 'yourpath'
excel_data_df = pandas.read_excel(file_path, sheet_name='Stock')

json_str = excel_data_df['Symbol']

urlpre = "yourpre"
urlsub = "yoursub"

data = []


driver = webdriver.Chrome()
scrollElementIntoMiddle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);" \
                                                        + "var elementTop = arguments[0].getBoundingClientRect().top;" \
                                                        + "window.scrollBy(0, elementTop-(viewPortHeight/2));"

for value in json_str :
    try:
        url = str(urlpre)+str(value).lower()+str(urlsub)
        # Instantiate a WebDriver object (in this case, Chrome WebDriver)

        
        # Open webpage
        driver.get(url)

        svg_element = driver.find_element(by=By.CLASS_NAME, value="meter")
        driver.execute_script(scrollElementIntoMiddle, svg_element)

        polygon = svg_element.find_element(by=By.TAG_NAME, value="polygon")
        polygon_style = polygon.get_attribute('style')

        transform_style = ""
        rotate_value = 0
        if polygon_style:
            styles = polygon_style.split(";")
            for style in styles:
                if "transform" in style:
                    match = re.search(r'rotate\(([-+]?\d*\.?\d+)\s*deg\)', style)
                    if match:
                        rotate_value = float(match.group(1))
                    transform_style = style.strip()

       
        print("++++++++++++++"+str(rotate_value)+"+++url : "+str(url))
    except NoSuchElementException:
        print("------------1Not Found Element : "+str(url))
        continue
    
driver.quit()   