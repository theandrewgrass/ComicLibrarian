class Page:
    def __init__(self, page_content, page_number):
        self.page = page_content
        self.page_number = page_number
        self.dimensions = self.get_page_dimensions()

    def get_page_dimensions(self):
        return self.page.size

    def __str__(self):
        return f'Page Number: {self.page_number}, Dimensions (width, height): {self.dimensions}'
