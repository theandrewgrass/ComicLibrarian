import re

class UserStrings:
    greetings = "Greetings form the Comic Librarian!"
    what_to_search = "What do you want to search for? "
    report_results = "{num_matches} results were returned by your search:"
    which_title = "Which title from the following would you like to get? "
    find_issues = "I will find you issues for the title, {title}"
    odd_result_index = "{index}. {result}"
    even_result_index = "{index:4d}. {result:55s}"
    which_issue = "Which issue from the following would you like to get? "


class ProgressUpdateStrings:
    start_machine = "Starting up the Library Machine..."
    boot_catalogue = "Booting up the catalogue..."
    search_item = "Searching for titles similar to {item}..."
    open_title = "Opening the title page for {title}..."
    open_issue = "Opening the page for {issue} from the title, {title}..."
    get_metadata = "Getting the comic's metadata..."
    get_content = "Getting the issue's content..."
    show_book = "Here is the comic that's been built:"


class WebElements:
    site_url = "https://readcomiconline.to"
    comic_sub_url = "Comic"
    search_form_id = "keyword"
    content_filter_tag = "tr"
    issues_class = "listing"
    book_metadata_class = "barContent"
    metadata_type_class = "info"
    div_tag = "div"
    a_tag = "a"
    p_tag = "p"
    span_tag = "span"
    class_attribute = "class"
    lxml_string = "lxml"
    multi_value_class = "dotUnder"
    high_quality = "hq"
    all_pages_read_type = "1"
    issue_url = f'{site_url}/{comic_sub_url}/{("{title}/{issue}?quality={quality}&readType={read_type}")}'
    image_selector = "#divImage > p > img"
    img_tag = "img"
    rel_attribute = "rel"
    no_referrer_value = "noreferrer"
    src_attribute = "src"

class FormattingStrings:
    nb_space = "&nbsp;"
    repeated_spaces = "\s\s+"
    repeated_dashes = "--+"
    space_string = " "
    colon_string = ":"
    dash_string = "-"
    unwanted_chars = [' ', ',', '.', '?', '!', ':', ';', ')', '(', '\'', '/', '"', '#', '_', '+']

    def format_content_for_url(self, content):
        for char in self.unwanted_chars:
            content = content.replace(char, self.dash_string)

        while content.endswith(self.dash_string):
            content = content[:-1]

        while content.startswith(self.dash_string):
            content = content[1:]

        content = re.sub(self.repeated_dashes, self.dash_string, content)

        return content

class MetadataElements:
    genres = "Genres"
    writer = "Writer"
    artist = "Artist"
    publisher = "Publisher"
    publication_date = "PublicationDate"
    summary = "Summary"