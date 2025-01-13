from magazine import Magazine
from publication import Publication

def test_magazine():
    authors = ["Vivienne Lancaster", "Aubrey Joan", "Tina Newark"]
    tv = Magazine("Teen Vogue, Decemeber 2017", authors, 3.50, "Advance Publications", "quarterly", "teens")

    assert isinstance(tv,Magazine)
    assert isinstance(tv, Publication)