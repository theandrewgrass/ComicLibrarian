from Librarian import Librarian

try:
    comic_librarian = Librarian()
    search_request = comic_librarian.get_search_request()
    comic_librarian.find_requested_item(search_request)
    comic_librarian.get_title_request()
    comic_librarian.go_to_title_page()
    comic_librarian.find_available_issues()
    comic_librarian.get_issue_request()
    comic_librarian.get_comic()
finally:
    comic_librarian.browser.close_browser()
