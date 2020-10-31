from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

path = "C:/Users/user/Desktop/sparta/projects/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.youtube.com")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.implicitly_wait(6)

elem = driver.find_element_by_name("search_query")
elem.send_keys('bbcnews')

elem.send_keys(Keys.RETURN)
# driver.find_element_by_xpath("//form[@class='ui form']/button").send_keys(Keys.ENTER)

driver.implicitly_wait(5)
fil = driver.find_element_by_css_selector('#container > ytd-toggle-button-renderer > a')
fil.click()

#label > yt-formatted-string
#collapse-content
fil_under_4m = driver.find_element_by_css_selector('div[title="단편(4분 이하) 검색"]')
fil_under_4m.click()

#button > yt-icon

#contents > ytd-item-section-renderer
#video-title > yt-formatted-string


#dismissable
driver.implicitly_wait(7)
vedio_list = driver.find_element_by_css_selector('#contents > div.text-wrapper')
print(vedio_list.text)
# for video in vedio_list:
#     print(video.text)
#video-title > yt-formatted-string

#video-title
#video-title

# scrib = driver.find_element_by_css_selector('button > yt-icon')
# scrib.click()

# fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
#
# count = 0
# for fruit in fruits:
#     if fruit == '사과':
#         count += 1
#
# # 사