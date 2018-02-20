'''
Created on Feb 23, 2015

@author: xiaoma
'''

from selenium import webdriver
from bs4 import BeautifulSoup
from methods import BeautifulSoup,getPageSource
import os
import time
from mhlib import isnumeric

DIR = os.getcwd().replace("\\","/")
IN_FILE = "/UserIDs.csv"
OUT_FILE = "/Corrected.UserIDs.csv"

def main():
    # an instance of Firefox driver
    driver = webdriver.Firefox()
    # visit TurkerNation.com, and log in
    driver.get("http://TurkerNation.com/")
    # toggle the invisible login form
    inputLoginForm = driver.find_element_by_id("multix_login_form_link")
    inputLoginForm.click()
    time.sleep(1)
    # fill in User Name and Password
    inputUsername = driver.find_element_by_name("vb_login_username")
    inputUsername.send_keys("Shogun_Sean")
    inputPassword = driver.find_element_by_name("vb_login_password")
    inputPassword.send_keys("xiaoma830514")
    inputPassword.submit() # submitting the Password text box automatically clicks the "login" button
    time.sleep(5)

    with open(DIR+OUT_FILE, "w") as fin:
        fin.write("")
    
    # find all user profile paths with "-" in UserID
    with open(DIR+IN_FILE, "r") as fin:
        for line in fin.readlines():
            line = line.strip()
            if "-" not in line:
                continue
            try:
                profile_url = ""
                profile_url = "http://turkernation.com/member.php?" + line.split(",")[0] + "-" + line.split(",")[1]
            except:
                print "\nParse error!"
                continue
            html = ""
            html = getPageSource(driver, profile_url).encode("UTF-8") # an exception handler is already included in the method
            if len(html)==0:
                print "\nHTML get page source error!"
                continue
            # instantiate a soup
            soup = BeautifulSoup(html)
            try:
                class_member_username = soup.find(attrs = {"class": "member_username"})
                correct_username = ""
                correct_username = class_member_username.get_text()
            except:
                print "\nBeautiful Soup error!"
                continue
            with open(DIR+OUT_FILE, "a") as saveCorrectUsername:
                saveCorrectUsername.write(line.split(",")[0] + "," + line.split(",")[1] + "," + correct_username + "\n")

    print "Success!"
    time.sleep(10)
    driver.close()

if __name__ == '__main__':
    main()