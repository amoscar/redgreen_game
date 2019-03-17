"""
This module contains the classes used to hold the data to play the Red/Green Game.
"""

class GameStyle:
    """
    A class to define the set-up information for the game.
    """

    def __init__(self):
        self._number_teams = 0

    @property
    def number_teams(self):
        return self._number_teams

    @number_teams.setter
    def number_teams(self, teams):
        """This method sets the number of teams"""
        if type(teams) == int:
            if teams == 4:
                self._number_teams = 4
            elif teams == 5:
                self._number_teams = 5
            else:
                raise ValueError('Number of allowable teams must be 4 or 5')
        else:
            raise TypeError('Number of allowable teams must be an integer')
