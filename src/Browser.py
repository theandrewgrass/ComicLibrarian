from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import os

from StringResource import WebElements, FormattingStrings
from Extractor import ResultExtractor, MetadataExtractor, ImageExtractor
from ImageDownloader import ImageDownloader


class Browser:
    def __init__(self):
        self.driver = self.setup_driver()
        self.results = {
            "search_results": None,
            "issue_results": None
        }

    def setup_driver(self):
        path_to_chrome_driver = os.path.abspath(r'..\chromedriver\chromedriver.exe')
        os.environ["webdriver.chrome.driver"] = path_to_chrome_driver
        #path_to_ad_block = r'D:\Programming\Python\ScrapingComics\1.16.4_0'
        chrome_options = Options()
        #chrome_options.add_argument(f'load-extension={path_to_ad_block}')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--incognito')
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
        self.record_results("search_results")

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

    def record_results(self, results_type):
        html = self.driver.page_source
        self.results[results_type] = ResultExtractor().extract_available_content_from_html(html)

    def get_results(self, results_type):
        return self.results[results_type]

    def go_to_title_page(self, title):
        url_formatted_title = FormattingStrings().format_content_for_url(title)
        base_url = WebElements.site_url
        self.navigate_to_url(f'{base_url}/{WebElements.comic_sub_url}/{url_formatted_title}')

    def get_book_metadata(self):
        self.wait_for_metadata()
        html = self.driver.page_source
        book_metadata = MetadataExtractor().extract_book_metadata_from_html(html)

        return book_metadata

    def get_issues(self):
        self.wait_for_issues()
        self.record_results("issue_results")

    def wait_for_metadata(self):
        timeout = 10
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, WebElements.book_metadata_class)))

    def wait_for_issues(self):
        timeout = 10
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, WebElements.issues_class)))

    def get_images(self):
        self.wait_for_images()
        html = self.driver.page_source
        image_urls = ImageExtractor().extract_image_urls_from_html(html)

        images = [ImageDownloader().download_image_as_bytes(image_url) for image_url in image_urls]

        return images

    def wait_for_images(self):
        timeout = 10
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, WebElements.image_selector)))

    def go_to_issue_page(self, title, issue):
        url_formatted_title = FormattingStrings().format_content_for_url(title)
        url_formatted_issue = FormattingStrings().format_content_for_url(issue)

        # Consider getting quality from a config file of some sort
        full_url = WebElements.issue_url.format(
            title=url_formatted_title,
            issue=url_formatted_issue,
            quality=WebElements.high_quality,
            read_type=WebElements.all_pages_read_type
        )

        self.navigate_to_url(full_url)

    def close_browser(self):
        print("browser closing")
        self.driver.close()
        self.driver.quit()



