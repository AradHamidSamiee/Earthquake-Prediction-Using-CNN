from selenium import webdriver
from datetime import datetime
import time

now = datetime.now()
TimeAnchor = now.strftime("%d %m %Y")
month = int(TimeAnchor.split()[1])
year  = int(TimeAnchor.split()[2])
# day   = int(TimeAnchor.split()[0])
day = 1

url = "https://earthquake.usgs.gov/earthquakes/search/"
Japan = (36.2048,138.2529,900)
TimeStart  = str(year) + "-" + str(month) + "-" + str(day) + " " + "00:00:00"
TimeFinish = TimeStart
# open browser
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)
# click button - Custom Date & Time
browser.find_element_by_xpath('//*[@id="fdsn-search-form"]/section/div[2]/section/ul[1]/li[3]/label').click()
# input text - Custom Date & Time
browser.find_element_by_xpath('//*[@id="starttime"]').clear()
browser.find_element_by_xpath('//*[@id="starttime"]').send_keys(TimeStart)
browser.find_element_by_xpath('//*[@id="endtime"]').clear()
browser.find_element_by_xpath('//*[@id="endtime"]').send_keys(TimeFinish)
# click button - Advanced Options
browser.find_element_by_xpath('//*[@id="search-advanced"]').click()
# input text - Custom Depth
browser.find_element_by_xpath('//*[@id="mindepth"]').send_keys("0")
browser.find_element_by_xpath('//*[@id="maxdepth"]').send_keys("250")
# input text - Custom Circular Coordinates
browser.find_element_by_xpath('//*[@id="latitude"]').send_keys(str(Japan[0]))
browser.find_element_by_xpath('//*[@id="longitude"]').send_keys(str(Japan[1]))
browser.find_element_by_xpath('//*[@id="maxradiuskm"]').send_keys(str(Japan[2]))
# click button - Event Type
browser.find_element_by_xpath('//*[@id="evttype"]').click()
browser.find_element_by_xpath('//*[@id="fdsn-search-form"]/div[1]/section/div/div[3]/section[1]/ul/li[1]/label').click()
browser.find_element_by_xpath('//*[@id="fdsn-search-form"]/div[1]/section/div/div[3]/section[1]/ul/li[2]/ul/li[40]/label').click()
browser.find_element_by_xpath('//*[@id="fdsn-search-form"]/div[1]/section/div/div[3]/section[1]/ul/li[2]/ul/li[41]/label').click()
# click button - Output Options
browser.find_element_by_xpath('//*[@id="search-output"]').click()
browser.find_element_by_xpath('//*[@id="fdsn-search-form"]/div[2]/section/section[1]/ul/li[2]/label').click()
browser.find_element_by_xpath('//*[@id="fdsn-search-form"]/div[2]/section/section[2]/ul[1]/li[2]/label').click()
browser.find_element_by_xpath('//*[@id="limit"]').send_keys(20000)
