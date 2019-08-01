from Page import Page

class Book:
    def __init__(self):
        self.bookDetails = {
            "title": None,
            "author": None,
            "publisher": None,
            "genre": None,
            "numberPages": None, # integer
            "pages": None, # list of Pages
            "seriesUrl": None,
            "bookUrl": None
        }
    
    '''
    '   Takes a book detail (ie. title, author, etc.)
    '   This probably goes in a controller
    '''
    def SetBookDetails(self, detail):
        for key, value in detail.items():
            self.bookDetails.update({key: value})
