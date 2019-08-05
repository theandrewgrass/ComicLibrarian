from Page import Page


class Book:
    def __init__(self):
        self.Title = None  # regular title
        self.OtherName = None  # other names -- if any?
        self.Issue = None
        self.Writer = []
        self.Artist = []
        self.Publisher = None
        self.Genres = []
        self.PublicationDate = None
        self.Status = None  # Complete/incomplete -- is the series ongoing
        self.Summary = None
        self.NumberPages = None
        self.Pages = []
        # debate whether to keep these... can be derived
        self.BookUrl = None
        self.IssueUrl = None

    def to_string(self):
        for prop, value in book.__dict__.items():
            print(f'{prop}: {value}')
