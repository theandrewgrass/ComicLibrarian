from StringResource import UserStrings, ProgressUpdateStrings, WebElements
from Book import Book
from Extractor import MetadataExtractor, ResultExtractor
from Browser import Browser


class Librarian:
    def __init__(self):
        self.browser = self.get_browser()
        self.greet_user()
        self.boot_catalogue()
        self.book = Book()

    def get_browser(self):
        print(ProgressUpdateStrings.start_machine)
        return Browser()

    def greet_user(self):
        print(UserStrings.greetings)

    def boot_catalogue(self):
        print(ProgressUpdateStrings.boot_catalogue)
        self.browser.navigate_to_url(WebElements.site_url)

    def get_search_request(self):
        search_request = input(UserStrings.what_to_search)
        return search_request

    def find_requested_item(self, requested_item):
        print(ProgressUpdateStrings.search_item.format(item=requested_item))
        self.browser.search_for_item_using_form(requested_item)
        self.browser.record_results()
        self.report_results(self.browser.results)

    def report_results(self, results):
        max_string_length = 50
        num_results = len(results)

        print(UserStrings.report_results.format(num_matches=num_results))

        for i, result in enumerate(results):
            if len(result) > max_string_length:
                result = f'{result[:max_string_length]}...'

            if i % 2 == 0:
                formatted_result = UserStrings.even_result_index.format(
                    index=i + 1,
                    result=result
                )
                print(formatted_result, end='')

            else:
                formatted_result = UserStrings.odd_result_index.format(
                    index=i+1,
                    result=result
                )
                print(formatted_result)

        if num_results % 2 != 0:
            print("\n")

    def get_title_request(self):
        title_index = int(input(UserStrings.which_title))
        self.book.Title = ResultExtractor().extract_title_from_results(self.browser.results, title_index)

    def go_to_title_page(self):
        title = self.book.Title
        print(ProgressUpdateStrings.open_title.format(title=title))
        self.browser.go_to_title_page(title)

    def build_book_metadata(self):
        book_metadata = self.browser.get_book_metadata()

        for key, value in book_metadata.items():
            self.book.__dict__[key] = value
        
        print("Retrieved book metadata:")
        for key, value in self.book.__dict__.items():
            print(f'{key}: {value}')

    def find_available_issues(self):
        print(UserStrings.find_issues.format(title=self.book.Title))
        self.browser.get_issues()
        self.report_results(self.browser.results)

    def get_issue_request(self):
        issue_index = int(input(UserStrings.which_issue))
        self.book.Issue = ResultExtractor().extract_issue_from_results(self.browser.results, issue_index, self.book.Title)

    def go_to_issue_page(self):
        title = self.book.Title
        issue = self.book.Issue
        print(ProgressUpdateStrings.open_issue.format(title=title, issue=issue))
        self.browser.go_to_issue_page(title, issue)

    def get_images(self):
        self.browser.get_images()
