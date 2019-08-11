from Page import Page


class Book:
    def __init__(self):
        self.Title = None  # regular title
        self.Issue = None
        self.Writer = []
        self.Artist = []
        self.Publisher = None
        self.Genres = []
        self.PublicationDate = None
        self.Summary = None
        self.NumberPages = 0
        self.Pages = []
        # use these to serialize this search result
        # if future searches for same title are made, can refer to these
        # self.BookUrl = None
        # self.IssueUrl = None

    def __str__(self):
        book = str()

        for prop, value in self.__dict__.items():
            if type(value) is list:
                value = ',\n '.join(str(single_value) for single_value in value)

            book += f'{"-"*30}\n{prop}:\n {value}\n'

        return book
