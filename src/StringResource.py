class UserStrings:
    greetings = "Greetings form the Comic Librarian!"
    what_to_search = "What do you want to search for? "
    report_results = "{num_matches} results were returned by your search:"
    which_title = "Which title from the following would you like to get? "
    find_issues = "I will find you issues for the title, {title}"
    odd_result_index = "{index}. {result}"
    even_result_index = "{index:4d}. {result:55s}"


class ProgressUpdateStrings:
    start_machine = "Starting up the Library Machine..."
    boot_catalogue = "Booting up the catalogue..."
    search_item = "Searching for titles similar to {item}..."


class WebElements:
    site_url = "https://readcomiconline.to"
    search_form_id = "keyword"
    filter_tag = "tr"
    issues_class = "listing"
    unwanted_chars = [' ', ',', '.', '?', '!', ':', ';', ')', '(', '\'', '/', '"', '#', '_', '+']
