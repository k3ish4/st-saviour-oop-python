from publication import Publication

# create Book parent class
class Book(Publication):
    def __init__(self, title: str, authors: list, cost: float, publisher: str, genre: str, page_number: int):
       # use super init function and allow Book to inherit title, authors, cost, and publisher traits from Publication
       super().__init__(title, authors, cost, publisher)
       self.genre = genre
       self.page_number = page_number

    # define a function that gives a synopsis of the book
    def synopsis(self):
        print("The book " + self.title + " by " + self.authors + " is a story with " + self.genre + " themes.")