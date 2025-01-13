from periodical import Periodical

# create Newspaper class as a child of the Periodical class and define all it's properties
class Newspaper(Periodical):
    def __init__(self, title: str, authors: list, cost: float, publisher: str, time_interval: str, headlines: list):
        # use super init function to allow the newspaper to inherit title, authors, price, publisher, and time interval from the Periodical class
        super().__init__(title, authors, cost, publisher, time_interval)
        self.headlines = headlines

    # use *args to create a function that accepts multiple arguments and adds them to the list of headlines in the newspaper
    def add_headlines(self, *args):
        for arg in args:
            self.headlines.append(arg)

    # use the __str__ dunder function so that returning an instance of Newspaper will show all of the properties of the instance instead of its memory address
    def __str__(self):
        return f'title: {self.title} \nauthors: {str(self.authors)} \ncost: ${str(self.cost)} \npublisher: {self.publisher} \ntime interval: {self.time_interval} \nheadlines: {str(self.headlines)}'