class Person:
    def __init__(self, name, watched, friends, subscriptions):
        """watched is a list"""

        self.name = name
        self.watched = watched
        
        self.friends = friends
        self.subscriptions = subscriptions

    def add_watched(self, movie):
        """this will add a movie to the person's watched dictionary"""
        self.watched.append(movie)
    