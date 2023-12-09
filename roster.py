"""
Handles generating the competitors, leagues and holds the point_totals function.
"""

import competitor_class as cc

elIdolo = cc.create_competitor(cc.competitorDictionary["Andrade el Idolo"])
danielson = cc.create_competitor(cc.competitorDictionary["Bryan Danielson"])
kingston = cc.create_competitor(cc.competitorDictionary["Eddie Kingston"])
king = cc.create_competitor(cc.competitorDictionary["Brody King"])
castagnoli = cc.create_competitor(cc.competitorDictionary["Claudio Castagnoli"])
garcia = cc.create_competitor(cc.competitorDictionary["Daniel Garcia"])
briscoe = cc.create_competitor(cc.competitorDictionary["Mark Briscoe"])
mox = cc.create_competitor(cc.competitorDictionary["Jon Moxley"])
swerve = cc.create_competitor(cc.competitorDictionary["Swerve Strickland"])
rush = cc.create_competitor(cc.competitorDictionary["Rush"])
lethal = cc.create_competitor(cc.competitorDictionary["Jay Lethal"])
white = cc.create_competitor(cc.competitorDictionary["Jay White"])

blueLeague = cc.League("blue", [elIdolo, danielson, kingston, king, castagnoli, garcia])
goldLeague = cc.League("gold", [briscoe, mox, swerve, rush, lethal, white])

elIdolo.TBP = elIdolo.tieBreaker(blueLeague.roster)
king.TBP = king.tieBreaker(blueLeague.roster)
danielson.TBP = danielson.tieBreaker(blueLeague.roster)
castagnoli.TBP = castagnoli.tieBreaker(blueLeague.roster)
garcia.TBP = garcia.tieBreaker(blueLeague.roster)
kingston.TBP = kingston.tieBreaker(blueLeague.roster)

lethal.TBP = lethal.tieBreaker(goldLeague.roster)
white.TBP = white.tieBreaker(goldLeague.roster)
mox.TBP = mox.tieBreaker(goldLeague.roster)
briscoe.TBP = briscoe.tieBreaker(goldLeague.roster)
rush.TBP = rush.tieBreaker(goldLeague.roster)
swerve.TBP = swerve.tieBreaker(goldLeague.roster)

def point_totals(*leagues):
    """
Automatically formats the league participants into neat and tidy stat blocks.\n
Mathematically-eliminated competitors are marked with strikethrough text.
    """
    for league in leagues:
        print(f"{league.name.title()} League:")
        for guy in league.roster:
            while len(guy.name) < 24:
                guy.name += " "
            if guy.losses >= 3:
                print("\u0336" + "\u0336".join(f"{guy.name}: {str(guy.points).zfill(2)} points ({guy.wins}-{guy.losses}-{guy.draws})"))
            else:
                print(f"{guy.name}: {str(guy.points).zfill(2)} points ({guy.wins}-{guy.losses}-{guy.draws})", f"TBPs: {guy.TBP}", sep = "|")
        print()
