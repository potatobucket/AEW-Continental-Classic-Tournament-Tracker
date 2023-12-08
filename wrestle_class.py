"""
Classes for Wrestlers and Leagues. Also home to the create_wrestler function and wrestleDictionary.
"""

import csv

class Wrestler:
    """
Creates a wrestler with stats for a round-robin-style tournament.\n
Keeps track of points earned, wins, losses and draws.\n
In the event of a tie, tiebreaker points (TBP) can be calculated by passing in\n
the opponents to the tiebreaker function.
    """
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.opponentPoints = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.TBP = 0

    def tieBreaker(self, opponents = []):
        """
    Calculates tiebreaker points (TBP) for the wrestler. Pass in a list of opponents in the league.

    (Can pass a League object's roster with league.roster)
        """
        for opponent in opponents:
            if opponent.name != self.name:
                self.opponentPoints += opponent.points
        return self.opponentPoints

    def __lt__(self, other):
        return self.name < other.name
    
    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

class League:
    """
Keeps track of the wrestlers that are in the league.

Mostly used to keep separate stat blocks and calculate TBPs.
    """
    def __init__(
            self,
            roster = [
                Wrestler("Jim Jimerson"),
                Wrestler("James Jamerson"),
                Wrestler("Cliff Cliffton"),
                Wrestler("Greg Gregerson"),
                Wrestler("Al Jolson"),
                Wrestler("Xavier Cougat the Mambo King")
            ]
        ):
        self.roster = sorted(roster)
        self.matchList = []

    @property
    def matches(self):
        """
    (Note: depricated but kept because it took a while to figure out and I feel nice about it)
        """
        self.matchList = [
            (leftOpponent, rightOpponent) for leftOpponent in self.roster for rightOpponent in self.roster if leftOpponent != rightOpponent and (rightOpponent, leftOpponent) not in self.matchList
        ]
        return self.matchList

with open("wrestlers.csv", "r") as wrestlers:
    csvReader = csv.DictReader(wrestlers)

    wrestleDictionary = {
        line["wrestler"] : {
            "name" : line["wrestler"],
            "points" : line["points"],
            "wins" : line["wins"],
            "losses" : line["losses"],
            "draws" : line["draws"]
        } for line in csvReader
    }

def create_wrestler(guy = dict()):
    """
Pass a wrestler from the CSV dictionary into this function to\n
automatically populate a Wrestler object with the relevent info!
    """
    wrestler = Wrestler(guy["name"])
    wrestler.points = int(guy["points"])
    wrestler.wins = int(guy["wins"])
    wrestler.losses = int(guy["losses"])
    wrestler.draws = int(guy["draws"])
    return wrestler
