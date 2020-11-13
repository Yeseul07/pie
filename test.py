from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from flask import jsonify
from pymongo import MongoClient
import datetime
import time

path = "C:/Users/user/Desktop/sparta/projects/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.youtube.com")
client = MongoClient('localhost', 27017)
db = client.youtubeEng

# bbcnews 검색
elem = driver.find_element_by_name("search_query")
elem.send_keys('bbcnews')
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(6)

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# 검색 필터 설정
driver.find_element_by_css_selector('#container > ytd-toggle-button-renderer > a').click()
driver.find_element_by_css_selector('div[title="단편(4분 이하) 검색"]').click()
driver.implicitly_wait(5)

# # 스크롤을 내려야 이미지를 가져올 수 있기 때문에 스크롤을 몇번 내려준다.
ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.END).perform()
driver.implicitly_wait(5)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.implicitly_wait(5)

content_area = driver.find_element_by_css_selector('div.style-scope ytd-item-section-renderer')
content_list = content_area.find_elements_by_css_selector('div.style-scope ytd-video-renderer')

print('content count : {}'.format(len(content_list)))
# 스크랩할 컨텐트 카운트
target_content = 20
count = 0

# 스크랩할 유튜브 영상 수
for content in content_list[:target_content]:
    try:
        index = '{}번째 영상'.format(count)
        yt_thumb_src = content.find_element_by_id('img').get_attribute('src')
        yt_movie_src = 'https://youtube.com' + content.find_element_by_id('thumbnail').get_attribute('href')
        yt_movie_title = content.find_element_by_id('video-title').get_attribute('aria-label')
        # print(yt_thumb_src)
        if not yt_thumb_src:
            # print(yt_thumb_src)
        # else:
        #     elseprint('이미지가 없습니다')
            yt_thumb_src = ''
        # if yt_movie_src:
        #     print(yt_movie_src)
        # else:
        #     print('영상 주소가 없습니다')
        # if yt_movie_title:
        #     print(yt_movie_title)
        # else:
        #     print('영상 제목이 없습니다')

        # count 1 추가
        count += 1

        db.youtube.insert_one({
            'img': yt_thumb_src,
            'url': yt_movie_src,
            'title': yt_movie_title,
            'index': index
        })

    except StaleElementReferenceException:
        print('ignore StaleElement')



# #
# print(yt_movie_title)
# mongoDB에 데이터를 넣기



