from Book import Book
from StringResource import WebElements, MetadataElements, FormattingStrings
from bs4 import BeautifulSoup, SoupStrainer

import re


class ResultExtractor:

    def extract_available_content_from_html(self, html):
        content_filter = SoupStrainer(WebElements.content_filter_tag)
        filtered_html = BeautifulSoup(html, WebElements.lxml_string, parse_only=content_filter)
        filtered_elements = []

        for filtered_element in filtered_html:
            try:
                filtered_elements.append(filtered_element.find(WebElements.a_tag).get_text())
            
            except AttributeError:
                pass

        results = [FormattingStrings.space_string.join(html_result.split()) for html_result in filtered_elements]

        return results

    def extract_title_from_results(self, results, title_index):
        title = results[title_index-1]
        return title

    def extract_issue_from_results(self, results, issue_index, title):
        issue = results[issue_index-1].split(title)[1].replace(' ', '')
        return issue


class MetadataExtractor:

    metadata_types = list(Book().__dict__.keys())

    def extract_book_metadata_from_html(self, html):
        book_metadata_elements_filter = SoupStrainer(WebElements.div_tag, {WebElements.class_attribute: WebElements.book_metadata_class})
        filtered_html = BeautifulSoup(html, WebElements.lxml_string, parse_only=book_metadata_elements_filter)
        book_metadata = {}

        for filtered_element in filtered_html.findAll(WebElements.p_tag, {WebElements.class_attribute: None}):
            try:
                metadata_type_element = filtered_element.find(WebElements.span_tag, {WebElements.class_attribute: WebElements.metadata_type_class})
                metadata_type = re.sub(f'{FormattingStrings.space_string}|{FormattingStrings.colon_string}', str(), metadata_type_element.get_text().title())
            
            except AttributeError:
                continue

            if metadata_type in [MetadataElements.genres, MetadataElements.writer, MetadataElements.artist]:
                metadata = [metadata_element.get_text().title() for metadata_element in filtered_element.findAll(WebElements.a_tag, {WebElements.class_attribute: WebElements.multi_value_class})]
            
            elif metadata_type == MetadataElements.publisher:
                metadata_element = filtered_element.find(WebElements.a_tag, {WebElements.class_attribute: WebElements.multi_value_class})
                metadata = metadata_element.get_text().title()
            
            elif metadata_type == MetadataElements.publication_date:
                filtered_element.span.decompose()
                metadata = re.sub(f'{FormattingStrings.repeated_spaces}|{FormattingStrings.nb_space}', str(), filtered_element.get_text())
            
            elif metadata_type == MetadataElements.summary:
                metadata_element = filtered_element.find_next(WebElements.p_tag)
                metadata = metadata_element.get_text()
            
            else:
                continue

            book_metadata.update({metadata_type: metadata})

        return book_metadata

class ImageExtractor:
    def extract_image_urls_from_html(self, html):
        image_elements_filter = SoupStrainer(WebElements.img_tag, {WebElements.rel_attribute: WebElements.no_referrer_value})
        filtered_html = BeautifulSoup(html, WebElements.lxml_string, parse_only=image_elements_filter)

        image_urls = [image_element[WebElements.src_attribute] for image_element in filtered_html.find_all(WebElements.img_tag)]

        print(f'{len(image_urls)} urls were found:')
        for url in image_urls:
            print(url)

        return image_urls