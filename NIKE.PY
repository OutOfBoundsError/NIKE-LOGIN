from selenium import webdriver
from tkinter import Tk
from tkinter.filedialog import *
import selenium
import os
import time


os.chdir('C:\\#####\\#####\\#####\\#######\\#######') #Set to directory of your files including the script & proxies.txt & account.txt

site = 'http://www.nike.com/launch/' #change to product link

accounts= []
proxies = []

with open('proxies.txt') as proxies_list:
    proxies = proxies_list.read().splitlines()

with open('account.txt') as account_list:
    accounts = account_list.read().splitlines()


def loginNIKE(account_info):
    user = account_info.split(':')[0]
    passw = account_info.split(':')[1]
    
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.get(site)
    driver.maximize_window()
    driver.find_element_by_xpath("//a[@aria-label='Join or Log In']").click() # Clicks Login Button to open up the login MENU

    #enters account info
    driver.find_element_by_name("emailAddress").send_keys(user)
    driver.find_element_by_name("password").send_keys(passw)

    driver.find_element_by_xpath("//input[@value='LOG IN']").click()
    #time.wait(5)


def login(username, pword, driver):
    
    driver.find_element_by_name("emailAddress").send_keys(username)
    driver.find_element_by_name("password").send_keys(pword)

    driver.find_element_by_xpath("//input[@value='LOG IN']").click()

    if checkPhoneVerification(driver) == True:
        verifyPhone(driver, "4159198688")

    try: 
        driver.find_element_by_xpath("//a[@aria-label='Join or Log In']")
        print ('Unsuccessfully Log in.')
    except:
        print('Successfully Logged in.')



def checkAccess(link, account_info):
    user = account_info.split(':')[0]
    passw = account_info.split(':')[1]
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.get(link)
    driver.maximize_window()
    #access = False
    time.sleep(5)
    login(user, passw, driver)
    time.sleep(5)
    access_html = driver.page_source
    html_toString = str(access_html)

    if "Restricted Access" in html_toString:
        print("No Access")
        time.sleep(1)
    else:
        print("Have Access")
        print ("Username: " + user)
        print ("Password: " + passw)

    
    driver.quit()

def checkPhoneVerification(driver): #incomplete still need to fix it so that it loops until it is fully completed to verify.
    try:
        driver.find_element_by_xpath("//input[@placeholder='Mobile Number']")
        return True
    except:
        return False
    
def verifyPhone(driver, phoneNumber):
    driver.find_element_by_xpath("//input[@placeholder='Mobile Number']").send_keys(phoneNumber)
    driver.find_element_by_class_name("sendCodeButton").click()
    try:
        driver.find_element_by_class_name("error")
        print("PHONE NUMBER ERROR")
        new_phone_number = input("Enter another phone number: ")
        verifyPhone(driver, new_phone_number)
          
    
    except: 
        verify_code = raw_input('Enter the code sent to ' + phoneNumber)
        driver.find_element_by_xpath("//input[@placeholder='Enter Code']").send_keys(verify_code)
        driver.find_element_by_xpath("//input[@value='CONTINUE']").click()
        try:
            driver.find_element_by_class_name("error")
            print("Invalid Code")
            print("Requesting another code....")
            time.sleep(30)
            driver.find_element_by_class_name("sendCodeButton").click()
            new_verify_code = input("Enter the new code that was sent to your phone: ")
            driver.find_element_by_xpath("//input[@placeholder='Enter Code']").send_keys(new_verify_code)
            driver.find_element_by_xpath("//input[@value='CONTINUE']").click()
             
        except:
            print("Successfully verified.")









    
    
    




checkAccess('http://www.nike.com/launch/t/the-ten-air-jordan-1-off-white-powder-blue',accounts[0])









