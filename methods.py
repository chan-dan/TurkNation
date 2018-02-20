'''
Created on Oct 8, 2014

@author: xiaoma
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from Tkinter import Tk
import pyperclip
import csv


# getPageSource opens a webpage and saves the page source
def getPageSource(webdriver,url):
    # opens url
    webdriver.get(url)
    time.sleep(3) # wait for 3 seconds for page to load
    try:
        return webdriver.page_source
    except:
        print "\nHTML get page source error!"

def saveData(html):
    # instantiate a soup
    soup = BeautifulSoup(html)
    # find all <a> (hyperlinks) with class "username"
    profiles = soup.find_all(attrs = {"class": "username"})
    # lists
    lProfiles = []
    # in each <a>
    for profile in profiles:
        try:
            username = profile.a['href']
        except:
            pass
        if username == "":
            pass
        else:
            lProfiles.append(username)
            username = ""
    return lProfiles


def parseData(driver,html):
    # instantiate a soup
    soup = BeautifulSoup(html)
    moreactivity = driver.find_element_by_id("moreactivitylink")
        
    asuser=driver.find_element_by_id("asuser")
    asuser.click()
    
    while moreactivity.text != "":
        moreactivity.click()
    # find all <div>  with class "content hasavatar"
    profiles = soup.find_all(attrs = {"class": "content hasavatar"})
    # lists
    lProfiles = []
    # in each <a>
    for profile in profiles:
        try:
#             print profile
            datetime = profile.span.text
            datecombo = (datetime.strip()).split(",")
            replied = profile.find("div",{"class": "title"})
            name=replied.a["href"]
            firsta=replied.a
            subforum = firsta.findNext("a")
            subforum=subforum.findNext("a")
            subforum=subforum["href"]
            subforum=subforum.split("?")
            id = profile.find("div",{"class": "fulllink"})
            linkcontent = id.a
            linktext = linkcontent["href"]
            startedvalue=linktext
            idcombo=linktext.split("&")

            
            ######-----------------------
            
            resp = (replied.text.strip()).encode("utf-8")
            if "replied" in resp:
                resp="replied";
            if "started" in resp:
                resp= "started"
            name= name.split("?")
            username=name[1]
            date=(datecombo[0].strip()).encode("utf-8")
            time=(datecombo[1].strip()).encode("utf-8")
            justtime=time.decode("utf-8").encode("latin-1").decode("utf-8")
            time= justtime.strip()
            time = time.encode("utf-8")
            threadid = (idcombo[0].strip()).encode("utf-8")
            threadnum = threadid.split("?")
            threadnum = (threadnum[1]).encode("utf-8")
            if resp == "started":
                uniqueid=startedvalue.split("?")
                uniqueid=uniqueid[1]
            else:
                uniqueid = (idcombo[1].strip()).encode("utf-8")
                uniqueid=uniqueid.split("#")
                uniqueid=(uniqueid[0]).split("=")
                uniqueid=uniqueid[1]
                
            subforumid=subforum[1]
#             lProfiles.append("\n")
            lProfiles.append(date)
            lProfiles.append(time)
            lProfiles.append(username)
            lProfiles.append(threadnum)
            lProfiles.append(subforumid)
            lProfiles.append(uniqueid)
            lProfiles.append(resp)
            lProfiles.append("\n\r")
            
        except:
            pass
        
            datetime = ""
            datecombo = ""
            replied = ""
            id = ""
            linkcontent = ""
            linktext = ""
            idcombo = ""
            time = ""
            date = ""
            threadid = ""
            uniqueid = ""
            resp = ""
            
        writeintocsv(lProfiles)
            
    return lProfiles



def getDetails(driver,html):
    # instantiate a soup
    
    threadsbyuser = driver.find_element_by_link_text("Find threads started by this user")
    threadsbyuser.click()
    currentUrl = (driver.current_url)
    currentUrl=currentUrl.strip()
    html=getPageSource(driver, currentUrl)
    # find all <div>  with class "content hasavatar"
    soup = BeautifulSoup(html,from_encoding='utf-8')
    profiles = soup.find_all(attrs = {"class": "rating0"})
    print profiles
    lProfiles = []
    # in each <a>
    for profile in profiles:
        try:
            if profile.find("span",{"class": "prefix understate"}):
                sticky = "sticky"
            else:
                sticky = "not sticky"
            labeltag=profile.find("span",{"class": "label"})
            byuser=(labeltag.text).encode("utf-8")
            byuser=byuser.split(",")
            username=labeltag.a["href"]
            username=username.split("?")
            
            forumdata=profile.find("div",{"class": "threadpostedin"})
            forumdata=forumdata.p.a["href"]
            forumdata=forumdata.split("?")
            
            replies=profile.find("li",{"class": "stats"})
            
            lastposted=profile.find("div",{"class": "threadinfo thread"})
            lastposted = (lastposted.a['title']).encode("utf-8")
            lastposted = lastposted.split(",")
            
            uniqueid=profile.find("a",{"class":"title"})
            uniqueid=uniqueid["href"]
            seperate=uniqueid.split("?")
            
            ulist=profile.find("ul",{"class":"threadstats"})
            lilist=ulist.li
            lilist=lilist.findNext("li")
           
            ######-----------------------
            todaysdate=time.strftime("%d/%m/%Y")
            todaystime=time.strftime("%H:%M:%S")
            forumid=(forumdata[1]).encode("utf-8")
            
            startedby=byuser[0]
            startedby=startedby.strip()
            startedby=startedby.split(" ")
            username=username[1]
            startedby=username 
            attime=byuser[1]
            attime = attime
            replies=(replies.text).encode("utf-8")
            views=(lilist.text).encode("utf-8")
            lastpost=(lastposted[1]).encode("utf-8")
            uniqueid=(seperate[1]).encode("utf-8")
            lProfiles.append(""+todaysdate+"")
            lProfiles.append(""+todaystime+"")
            lProfiles.append(""+forumid+"")
            lProfiles.append(""+sticky+"")
            lProfiles.append(""+startedby+"")
            lProfiles.append(""+attime+"")
            lProfiles.append(""+views+"")
            lProfiles.append(""+replies+"")
            lProfiles.append(""+lastpost+"")
            lProfiles.append(""+uniqueid+"")
            lProfiles.append("\n")
            
        except:
            pass
        
        todaysdate = ""
        todaystime= ""
        forumdata = ""
        forumid = ""
        sticky = ""
        startedby = ""
        attime = ""
        views = ""
        lastpost = ""
        lastposted = ""
        replies = ""
        ulist = ""
        uniqueid = ""
            
        writeintocsv2(lProfiles)
        
    return lProfiles


def writeintocsv2(lProfiles):
    csvfile = open("Profile2.csv", "w")
    csvWriter = csv.writer( csvfile )  #Defaults to the excel dialect
    csvWriter.writerow(lProfiles)
    csvWriter.writerow("\n")
#     file.close()   #Required, or the data won't get flushed to the file!

def writeintocsv(lProfiles):
    csvfile = open("Profile.csv", "w")
    csvWriter = csv.writer( csvfile, delimiter="," )  #Defaults to the excel dialect
#     csvWriter.writerow("date","time","username","threadnum","subforumid","uniqueid","reply or start")
    csvWriter.writerow(lProfiles)
#     csvWriter.writerow("\n")
#     file.close()   #Required, or the data won't get flushed to the file!

def obsolete(x):
    fin = open(os.getcwd()+'\\test.txt', 'w')
    fin.write('abc\n\n\nabcabcd')
    fin.close()
    
    fin = open(os.getcwd()+'\\test.txt', 'r')
    text = fin.read()
    fin.close()
    # r = Tk()
    # r.withdraw()
    # r.clipboard_clear()
    # r.clipboard_append(text)
    # print('copied into clipboard')
    # r.destroy()
    
    pyperclip.copy(text)
    print(pyperclip.paste())
    print('copied into clipboard')
    time.sleep(60)
