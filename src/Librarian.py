from StringResource import UserStrings, ProgressUpdateStrings, WebElements
from Book import Book
from Extractor import MetadataExtractor, ResultExtractor
from Browser import Browser
from BookFactory import BookFactory


class Librarian:
    def __init__(self):
        self.browser = self.get_browser()
        self.boot_catalogue()
        self.book_factory = BookFactory()

    def get_browser(self):
        print(ProgressUpdateStrings.start_machine)
        return Browser()

    def boot_catalogue(self):
        print(ProgressUpdateStrings.boot_catalogue)
        self.browser.navigate_to_url(WebElements.site_url)

    def get_search_request(self):
        search_request = input(UserStrings.what_to_search)
        return search_request

    def find_requested_item(self, requested_item):
        print(ProgressUpdateStrings.search_item.format(item=requested_item))
        self.browser.search_for_item_using_form(requested_item)
        self.report_results(self.browser.get_results("search_results"))

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
        search_results = self.browser.get_results("search_results")
        title = ResultExtractor().extract_title_from_results(search_results, title_index)
        self.book_factory.set_book_title(title)

    def go_to_title_page(self):
        title = self.book_factory.get_book_title()
        print(ProgressUpdateStrings.open_title.format(title=title))
        self.browser.go_to_title_page(title)

    def find_available_issues(self):
        title = self.book_factory.get_book_title()
        print(UserStrings.find_issues.format(title=title))
        self.browser.get_issues()
        results = self.browser.get_results("issue_results")
        self.report_results(results)

    def get_issue_request(self):
        issue_index = int(input(UserStrings.which_issue))
        issue_results = self.browser.get_results("issue_results")
        title = self.book_factory.get_book_title()
        issue = ResultExtractor().extract_issue_from_results(issue_results, issue_index, title)
        self.book_factory.set_issue(issue)

    def get_comic(self):
        print(ProgressUpdateStrings.get_metadata)
        metadata = self.browser.get_book_metadata()
        self.book_factory.set_metadata(metadata)

        title = self.book_factory.get_book_title()
        issue = self.book_factory.get_issue()
        print(ProgressUpdateStrings.open_issue.format(title=title, issue=issue))
        self.browser.go_to_issue_page(title, issue)

        print(ProgressUpdateStrings.get_content)
        comic_images = self.browser.get_images()
        self.book_factory.set_pages(comic_images)

        print(ProgressUpdateStrings.show_book)
        self.book_factory.show_book()
