class Publication:
    def __init__(self, title: str, author: str, cost: float, publisher: str):
        self.title = title
        self.author = author
        self.cost = cost
        self.publisher = publisher

        def read(self):
            print("You are now reading " + self.title)