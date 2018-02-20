'''
This program scrapes the user profile URLs from the member directory pages.

Created on Feb 10, 2015
@author: xiaoma
'''
from selenium import webdriver
import urllib2
from bs4 import BeautifulSoup
import os
import time
from methods import getPageSource,saveData, parseData


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
    # prepare
    url = "http://turkernation.com/member.php?15186-Shogun_Sean"
    
    new_url = url
    html = getPageSource(driver, new_url).encode("UTF-8")
    thd=parseData(driver,html);
#     print thd
        # backup page source as an HTML file
#     new_html_filename = html_filename + str(page) + ".html"
#         with open(new_html_filename, "w") as saveHtml:
#             saveHtml.write(html)
        # extract and save data
#     profiles = ""
#     for data in saveData(html):
#             profiles += data + "\n"
#     with open(profile_filename, "a") as saveProfile:
#             saveProfile.write(profiles)
    
    print "Success!"
    time.sleep(10)
    driver.close()

if __name__ == '__main__':
    main()