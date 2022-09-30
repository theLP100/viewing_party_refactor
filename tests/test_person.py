import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie


def test_append_movie_to_watched():
    # Arrange
    Fateneh = Person("Fateneh", [], [],[])
    Batman = Movie("Batman", "action", 4, "HBO")
    # Act
    Fateneh.add_watched(Batman)
    # Assert
    len(Fateneh.watched) == 1