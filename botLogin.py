#imports the webdriver from selenium
from selenium import webdriver
import os

#path of chromedriver

def startBot(username, password, url):
    path = "path of chromedriver"

    #opening the site in chrome
    driver.get(url)

    #find the id or name of class of
    #username by inspecting on username input
    drive.find_element_by_name(
        "id/class/name of username").send_keys(username)
    
    #find the password by inspecting on password input
    driver.find_element_by_name(
        "id/class/name of password").send_keys(password)


#driver code
username = "enter username"
password = "enter password"

# url of the site 
url = "Enter URL of site"

#call the function
startBot(username, password, url)