"""
Classes for Competitors and Leagues. Also home to the create_competitor function and competitorDictionary.
"""

import csv

class Competitor:
    """
Creates a competitor with stats for a round-robin-style tournament.\n
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
    Calculates tiebreaker points (TBP) for the competitor. Pass in a list of opponents in the league.

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
Keeps track of the competitors that are in the league.

Mostly used to keep separate stat blocks and calculate TBPs.
    """
    def __init__(
            self,
            roster = [
                Competitor("Jim Jimerson"),
                Competitor("James Jamerson"),
                Competitor("Cliff Cliffton"),
                Competitor("Greg Gregerson"),
                Competitor("Al Jolson"),
                Competitor("Xavier Cougat the Mambo King")
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

    competitorDictionary = {
        line["wrestler"] : {
            "name" : line["wrestler"],
            "points" : line["points"],
            "wins" : line["wins"],
            "losses" : line["losses"],
            "draws" : line["draws"]
        } for line in csvReader
    }

def create_competitor(guy = dict()):
    """
Pass a competitor from the CSV dictionary into this function to\n
automatically populate a Competitor object with the relevent info!
    """
    competitor = Competitor(guy["name"])
    competitor.points = int(guy["points"])
    competitor.wins = int(guy["wins"])
    competitor.losses = int(guy["losses"])
    competitor.draws = int(guy["draws"])
    return competitor
