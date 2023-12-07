import csv

class Wrestler:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.opponentPoints = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.TBP = 0

    def tieBreaker(self, opponents = []):
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
        self.matchList = [
            (leftOpponent, rightOpponent) for leftOpponent in self.roster for rightOpponent in self.roster if leftOpponent != rightOpponent and (rightOpponent, leftOpponent) not in self.matchList
            ]
        return self.matchList

class Match:
    def __init__(self, leftGuy, rightGuy):
        self.leftGuy = leftGuy
        self.rightGuy = rightGuy

    def win(self, winner):
        winner.points += 3
        winner.wins += 1

    def lose(self, loser):
        loser.points += 0
        loser.losses += 1

    def draw(self):
        self.leftGuy.points += 1
        self.rightGuy.points += 1
        self.leftGuy.draws += 1
        self.rightGuy.draws += 1

    def __repr__(self):
        return f"{self.leftGuy} vs. {self.rightGuy}"
        
    def __str__(self):
        return f"{self.leftGuy} vs. {self.rightGuy}"

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

def createWrestler(guy = dict()):
    wrestler = Wrestler(guy["name"])
    wrestler.points = int(guy["points"])
    wrestler.wins = int(guy["wins"])
    wrestler.losses = int(guy["losses"])
    wrestler.draws = int(guy["draws"])
    return wrestler
