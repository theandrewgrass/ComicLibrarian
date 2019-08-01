from Librarian import Librarian

comic_librarian = Librarian()
search_request = comic_librarian.get_search_request()
comic_librarian.search_for_items_similar_to_requested_item(search_request)
comic_librarian.report_results()
title_request = comic_librarian.get_title_request()
comic_librarian.find_issues_given_title_index(title_request)
comic_librarian.report_results()
