from newspaper import Newspaper
from periodical import Periodical

def test_newspaper():
    authors = ['John Doe', 'Mary Sue']
    headlines = ['LA Wildfire', 'Polar Vortex, East Coast']
    nyt = Newspaper('New York Times, January 2025', authors, 1.50, 'NYT', 'weekly', headlines)

    assert isinstance(nyt, Newspaper)
    assert isinstance(nyt, Periodical)

