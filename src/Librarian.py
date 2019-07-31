import StringResource
from LibraryMachine import LibraryMachine


class Librarian:
    def __init__(self):
        self.libraryMachine = self.get_library_machine()
        self.greet_user()
        self.boot_catalogue()

    def get_library_machine(self):
        print(StringResource.ProgressUpdateStrings.start_machine)
        return LibraryMachine()

    def greet_user(self):
        print(StringResource.UserStrings.greetings)

    def boot_catalogue(self):
        print(StringResource.ProgressUpdateStrings.boot_catalogue)
        self.libraryMachine.boot_catalogue()

    def get_search_request(self):
        search_request = input(StringResource.UserStrings.what_to_search)
        return search_request

    def search_for_items_similar_to_requested_item(self, requested_item):
        print(StringResource.ProgressUpdateStrings.search_item.format(item=requested_item))
        self.libraryMachine.search_for_item_in_catalogue(requested_item)

    def report_results(self):
        max_string_length = 50
        search_results = self.libraryMachine.results
        num_results = len(search_results)

        print(StringResource.UserStrings.report_results.format(num_matches=num_results))

        for i, result in enumerate(search_results):
            if len(result) > max_string_length:
                result = f'{result[:max_string_length]}...'

            if i % 2 == 0:
                print(StringResource.UserStrings.even_result_index.format(index=i+1, result=result), end='')
            else:
                print(StringResource.UserStrings.odd_result_index.format(index=i+1, result=result))

        if num_results % 2 != 0:
            print("\n")

    def get_title_request(self):
        title_request = int(input(StringResource.UserStrings.which_title))
        return title_request

    def find_issues_given_title_index(self, title_index):
        print(StringResource.UserStrings.find_issues.format(title=self.libraryMachine.results[title_index-1]))
        self.libraryMachine.find_issues_given_title_index(title_index)

