from Book import Book
from Page import Page
from PIL import Image
from StringResource import FormattingStrings

import os #implement a file helper to help with all this dir-related stuff

class BookFactory:
    def __init__(self):
        self.book = Book()
        self.file_path = os.getcwd() #have a comics dir already made and set that

    def set_book_title(self, title):
        self.book.Title = title
    
    def get_book_title(self):
        return self.book.Title

    def set_issue(self, issue):
        self.book.Issue = issue

    def get_issue(self):
        return self.book.Issue

    def set_metadata(self, metadata):
        for key, value in metadata.items():
            self.book.__dict__[key] = value

    def set_pages(self, images):
        for number, image in enumerate(images):
            page = Page(image, number + 1)
            self.book.Pages.append(page)
            self.book.NumberPages += 1

    def show_book(self):
        print(self.book)

    def build_book(self):
        file_safe_title_name = FormattingStrings().format_content_for_url(self.book.Title)
        temp_dir_path = os.path.join(self.file_path, "Comics", file_safe_title_name, self.book.Issue)
        
        if not os.path.exists(temp_dir_path):
            os.makedirs(temp_dir_path)

        for page in self.book.Pages:
            print(f'Saving page {page.page_number}/{self.book.NumberPages}')
            page.page.save(f'{os.path.join(temp_dir_path, str(page.page_number))}.png', 'PNG')