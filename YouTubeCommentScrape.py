import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def you_tube_comment_scrape(page_URL_String, name_of_url):

    page_url = page_URL_String
    comment_x_path = '//*[@id="content-text"]'
    author_x_path = '//*[@id="author-text"]/span'
    dates_x_path = '//*[@id="header-author"]/yt-formatted-string/a'

    driver = webdriver.Chrome()
    driver.get(page_url)

    # The parameters for the scroll
    SCROLL_PAUSE_TIME = 2
    CYCLES = 20

    # A delay to allow for the loading of the page
    # Amend appropriate to internet connection
    time.sleep(20)

    # Setting the scroll by 'html' element, i.e. the page. 
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.PAGE_DOWN)

    for i in range(CYCLES):
        html.send_keys(Keys.END)
        # Add a pause after each scroll action
        time.sleep(SCROLL_PAUSE_TIME)

    # Finding and retrieiving the elements by XPATH. 
    authors = driver.find_elements(By.XPATH, author_x_path)
    comments = driver.find_elements(By.XPATH, comment_x_path)
    dates = driver.find_elements(By.XPATH, dates_x_path)

    # Pulling out the individual text of the elements. 
    author = [author.text for author in authors]
    date = [date.text for date in dates]
    comment = [comment.text for  comment in comments]

    # A dict is made is so as to make a Pandas dataframe
    dict = {'URL': page_url, 'Author': author, 'Time of Posting': date, 'Comments': comment }

    all_results = pd.DataFrame(dict)

    # The file is save in the local directory. 
    all_results.to_excel(f'Comment_Results_{name_of_url}.xlsx')
















