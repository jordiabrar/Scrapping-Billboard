from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

link = "https://www.billboard.com/charts/hot-100/"

driver.set_window_size(1300, 5300)
driver.get(link)

time.sleep(5)

driver.save_screenshot("home.png")

content = driver.page_source

driver.quit()

data = BeautifulSoup(content, 'html.parser')

i = 1
for area in data.find_all('li', class_="lrv-u-width-100p"):
    print(i)
    judul = area.find('h3', class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
    artis = area.find('span', class_="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
    print(judul)
    print("by :")
    print(artis)
    i+=1
    print("======================")
    