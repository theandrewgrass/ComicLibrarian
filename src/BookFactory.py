from Book import Book
from Page import Page

class BookFactory:
    def __init__(self):
        self.book = Book()

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
