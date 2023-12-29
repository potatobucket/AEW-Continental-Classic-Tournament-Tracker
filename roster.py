"""
Handles generating the competitors, leagues and holds the point_totals function.
"""

import competitor_class as cc
from math import ceil

# an example of how to create a competitor and league---------------
example = cc.create_competitor(cc.competitorDictionary["Example"])

exampleLeague = cc.League("example", [example])

example.TBP = example.tieBreaker(exampleLeague.roster)
# ------------------------------------------------------------------

def point_totals(*leagues):
    """
Automatically formats the league participants into neat and tidy stat blocks.\n
Mathematically-eliminated competitors are marked with strikethrough text.
    """
    longestName = lambda leagueRoster: max([len(entrant.name) for entrant in leagueRoster])
    lossLimit = lambda leagueMembers: ceil((len(leagueMembers) - 1) / 2)
    for league in leagues:
        print(f"{league.name.title()} League:")
        for guy in league.roster:
            while len(guy.name) < longestName(league.roster):
                guy.name += " "
            if guy.losses >= lossLimit(league.roster):
                print("\u0336" + "\u0336".join(f"{guy.name}: {str(guy.points).zfill(2)} points ({guy.wins}-{guy.losses}-{guy.draws})"))
            else:
                print(f"{guy.name}: {str(guy.points).zfill(2)} points ({guy.wins}-{guy.losses}-{guy.draws})", f"TBPs: {guy.TBP}", sep = "|")
        print()
