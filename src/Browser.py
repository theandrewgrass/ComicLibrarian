from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import os
import re

from StringResource import WebElements, FormattingStrings
from Extractor import ResultExtractor, MetadataExtractor


class Browser:
    def __init__(self):
        self.driver = self.setup_driver()
        self.results = None

    def setup_driver(self):
        path_to_chrome_driver = os.path.abspath(r'..\chromedriver\chromedriver.exe')
        os.environ["webdriver.chrome.driver"] = path_to_chrome_driver
        #path_to_ad_block = r'D:\Programming\Python\ScrapingComics\1.16.4_0'
        chrome_options = Options()
        #chrome_options.add_argument(f'load-extension={path_to_ad_block}')
        #chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        args = ["hide_console", ]
        driver = webdriver.Chrome(chrome_options=chrome_options, service_args=args)

        return driver

    def navigate_to_url(self, url):
        print(f'Navigating to {url}...')
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

    def record_results(self):
        html = self.driver.page_source
        self.results = ResultExtractor().extract_available_content_from_html(html)

    def go_to_title_page(self, title):
        url_formatted_title = self.format_content_for_url(title)
        base_url = WebElements.site_url
        self.navigate_to_url(f'{base_url}/{WebElements.comic_sub_url}/{url_formatted_title}')

    def format_content_for_url(self, content):
        for char in FormattingStrings.unwanted_chars:
            content = content.replace(char, FormattingStrings.dash_string)

        while content.endswith(FormattingStrings.dash_string):
            content = content[:-1]

        while content.startswith(FormattingStrings.dash_string):
            content = content[1:]

        content = re.sub(FormattingStrings.repeated_dashes, FormattingStrings.dash_string, content)

        return content

    def get_book_metadata(self):
        self.wait_for_metadata()
        html = self.driver.page_source
        book_metadata = MetadataExtractor().extract_book_metadata_from_html(html)

        return book_metadata

    def get_issues(self):
        self.wait_for_issues()
        self.record_results()

    def wait_for_metadata(self):
        timeout = 10
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, WebElements.book_metadata_class)))

    def wait_for_issues(self):
        timeout = 10
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, WebElements.issues_class)))

    def go_to_issue_page(self, title, issue):
        url_formatted_title = self.format_content_for_url(title)
        url_formatted_issue = self.format_content_for_url(issue)
        base_url = WebElements.site_url

        self.navigate_to_url(f'{base_url}/{WebElements.comic_sub_url}/{url_formatted_title}/{url_formatted_issue}')

    def close_browser(self):
        print("browser closing")
        self.driver.close()
        self.driver.quit()



