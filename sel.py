from selenium import webdriver
from password import passw
from time import sleep
user = "kingshuk.mukherjee"


browser = webdriver.Chrome('C:/Users/asus/Downloads/chromedriver.exe')
browser.get('https://www.instagram.com/')
sleep(1.5)
browser.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys(user)
browser.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys(passw)
browser.find_element_by_xpath("//button[@type=\"submit\"]")\
    .click()
sleep(4)
browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
sleep(0.1)
browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
sleep(0.5)
browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
sleep(3)
browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a").click()


