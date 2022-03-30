from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

global driver

def surveyCode(code, time):
    chrome=Service('C:\Program Files (x86)\chromedriver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=chrome, options=options)
    driver.get("https://www.mykfcexperience.com/?AspxAutoDetectCookieSupport=1")

    # Turn time into Hour, Minute, and Meridian
    time = re.split(':| ',time)
    hour = time[0]
    minute = time[1]
    meridian = time[2]
    
    inputbox = driver.find_element(By.NAME, "CN1")
    inputbox.send_keys(code)
    
    inputbox = Select(driver.find_element(By.NAME, "InputHour"))
    inputbox.select_by_value (hour)
    
    inputbox = Select(driver.find_element(By.NAME, "InputMinute"))
    inputbox.select_by_value (minute)
    
    inputbox = Select(driver.find_element(By.NAME, "InputMeridian"))
    inputbox.select_by_value (meridian)
    
def main():
    # code = "S7200740330222361"
    # time = "01:06 PM"
    code = input("Enter KFC Survey Code: ").upper()
    time = input("Enter Visit Time(Format XX:XX PM/AM): ").upper()

if __name__ == "__main__":
    main()