from Browser import Browser
from StringResource import WebElements


class LibraryMachine:
    def __init__(self):
        self.browser = Browser()
        self.results = None


    def find_issues_given_title_index(self, title):
        self.browser.find_issues_given_title(title)
        self.results = self.browser.get_results()
