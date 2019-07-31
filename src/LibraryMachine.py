from Browser import Browser
import StringResource


class LibraryMachine:
    def __init__(self):
        self.browser = Browser()
        self.results = None

    def boot_catalogue(self):
        self.browser.navigate_to_url(StringResource.WebElements.site_url)

    def search_for_item_in_catalogue(self, requested_item):
        self.browser.search_for_item_using_form(requested_item)
        self.results = self.browser.get_results()

    def find_issues_given_title_index(self, title_index):
        title = self.results[title_index-1]
        self.browser.find_issues_given_title(title)
        self.results = self.browser.get_results()
