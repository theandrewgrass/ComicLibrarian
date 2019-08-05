from Book import Book
from StringResource import WebElements
from bs4 import BeautifulSoup, SoupStrainer

import re


class ResultExtractor:

    def extract_available_content_from_html(self, html):
        content_filter = SoupStrainer(WebElements.content_filter_tag)
        filtered_html = BeautifulSoup(html, "lxml", parse_only=content_filter)
        filtered_elements = []

        for filtered_element in filtered_html:
            try:
                filtered_elements.append(filtered_element.find('a').get_text())
            except AttributeError:
                pass

        results = [" ".join(html_result.split()) for html_result in filtered_elements]

        return results


class MetadataExtractor:

    metadata_types = list(Book().__dict__.keys())

    def extract_book_metadata_from_html(self, html):
        book_metadata_elements_filter = SoupStrainer("div", {"class": WebElements.book_metadata_class})
        filtered_html = BeautifulSoup(html, "lxml", parse_only=book_metadata_elements_filter)
        book_metadata = {}

        for filtered_element in filtered_html.findAll("p", {"class": None}):
            try:
                metadata_type = filtered_element.find("span", {"class": "info"}).get_text().title().replace(' ', '').strip(':')
            except AttributeError:
                continue

            if metadata_type in ["Genres", "Writer", "Artist"]:
                metadata = [genre.get_text().title() for genre in filtered_element.findAll("a", {"class": "dotUnder"})]
            elif metadata_type == "Publisher":
                metadata = filtered_element.find("a", {"class": "dotUnder"}).get_text().title()
            elif metadata_type == "PublicationDate":
                filtered_element.span.decompose()
                metadata = filtered_element.get_text().replace("&nbsp;", '')
                metadata = re.sub('\s\s+', '', metadata)
            elif metadata_type == "Summary":
                metadata = filtered_element.find_next("p").get_text()
            else:
                continue

            book_metadata.update({metadata_type: metadata})

        return book_metadata
