from periodical import Periodical

class Magazine(Periodical):
    def __init__(self, title: str, authors: list, cost: float, publisher: str, time_interval: str, target_audience: str):
        # use super init function to allow the magazine to inherit title, authors, price, publisher, and time interval from the Periodical class
        super().__init__(title, authors, cost, publisher, time_interval)
        self.target_audience = target_audience

    # define a function that flips through the magazine's pages
    def flip_page(self):
        print("You've just turned to the next page of your magazine titled " + self.title + ".")
