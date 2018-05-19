from selenium import webdriver
from tkinter import Tk
from tkinter.filedialog import *
import selenium
import os
import time


os.chdir('C:\\#####\\#####\\#####\\#####\\######') #Enter the directory containing both proxies.txt & account.txt

site = 'http://www.nike.com/launch/' #change to product link

accounts= []
proxies = []

with open('proxies.txt') as proxies_list:
    proxies = proxies_list.read().splitlines()

with open('account.txt') as account_list:
    accounts = account_list.read().splitlines()


def login(account_info):
    user = account_info.split(':')[0]
    passw = account_info.split(':')[1]
    
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)
    driver.get(site)
    driver.maximize_window()
    driver.find_element_by_xpath("//a[@aria-label='Join or Log In']").click() # Clicks Login Button to open up the login MENU

    #enters account info
    driver.find_element_by_name("emailAddress").send_keys(user)
    driver.find_element_by_name("password").send_keys(passw)

    driver.find_element_by_xpath("//input[@value='LOG IN']").click()
    time.wait(5)
    
    



login(accounts[0])









