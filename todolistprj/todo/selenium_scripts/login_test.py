from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Tauhid\\Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=s)