from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import os
import re

from StringResource import WebElements


class Browser:
    def __init__(self):
        self.driver = self.setup_driver()

    def setup_driver(self):
        path_to_chrome_driver = r'"C:\Users\agrass\AppData\Local\Programs\Python\Python37-32\Scripts\chromedriver.exe"'
        os.environ["webdriver.chrome.driver"] = path_to_chrome_driver
        #path_to_ad_block = r'D:\Programming\Python\ScrapingComics\1.16.4_0'
        chrome_options = Options()
        #chrome_options.add_argument(f'load-extension={path_to_ad_block}')
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        args = ["hide_console", ]
        driver = webdriver.Chrome(chrome_options=chrome_options, service_args=args)

        return driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def search_for_item_using_form(self, item):
        self.wait_for_search_form()
        form = self.find_search_form()
        form.send_keys(f'{item}{Keys.RETURN}')

    def wait_for_search_form(self):
        timeout = 10  # seconds
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.ID, WebElements.search_form_id)))

    # may have to add try catch depending on types of exceptions
    def find_search_form(self):
        search_form = self.driver.find_element_by_id(WebElements.search_form_id)
        search_form.click()
        search_form.clear()

        return search_form

    def get_results(self):
        html = self.driver.page_source
        results = self.extract_results_from_html(html)

        return results

    def extract_results_from_html(self, html):
        title_element_filter = SoupStrainer(WebElements.filter_tag)
        filtered_html = BeautifulSoup(html, "lxml", parse_only=title_element_filter)
        filtered_elements = []

        for filtered_element in filtered_html:
            try:
                filtered_elements.append(filtered_element.find('a').get_text())
            except AttributeError:
                pass

        results = [" ".join(html_result.split()) for html_result in filtered_elements]

        return results

    def find_issues_given_title(self, title):
        url_formatted_title = self.format_content_for_url(title)
        base_url = WebElements.site_url
        self.navigate_to_url(f'{base_url}/Comic/{url_formatted_title}')
        self.wait_for_issues()

    def format_content_for_url(self, content):
        for char in WebElements.unwanted_chars:
            content = content.replace(char, '-')

        while content.endswith('-'):
            content = content[:-1]

        while content.startswith('-'):
            content = content[1:]

        content = re.sub('--+', '-', content)

        return content

    def wait_for_issues(self):
        timeout = 10
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, WebElements.issues_class)))

    def close_browser(self):
        self.driver.close()
        self.driver.quit()



