from abc import ABC, abstractmethod

# create Publication grandparent class and define all its properties
class Publication(ABC):
    def __init__(self, title: str, authors: list, cost: float, publisher: str):
        self.title = title
        self.authors = authors
        self.cost = cost
        self.publisher = publisher
        
    # define a read function
    def read(self):
        return "You are now reading " + self.title + "."