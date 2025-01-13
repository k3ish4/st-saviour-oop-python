from publication import Publication

class Periodical(Publication):
    # use super init function and allow Periodical to inherit title, authors, cost, and publisher traits from Publication
    def __init__(self, title: str, authors: list, cost: float, publisher: str, time_interval: str):
        super().__init__(title, authors, cost, publisher)
        self.time_interval = time_interval

    # define a function that announces a newly released periodical
    def new_issue(self):
        print(self.publisher + " has just released a new " + self.time_interval + " issue titled " + self.title + ".")