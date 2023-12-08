import wrestle_class as wc

elIdolo = wc.createWrestler(wc.wrestleDictionary["Andrade el Idolo"])
danielson = wc.createWrestler(wc.wrestleDictionary["Bryan Danielson"])
kingston = wc.createWrestler(wc.wrestleDictionary["Eddie Kingston"])
king = wc.createWrestler(wc.wrestleDictionary["Brody King"])
castagnoli = wc.createWrestler(wc.wrestleDictionary["Claudio Castagnoli"])
garcia = wc.createWrestler(wc.wrestleDictionary["Daniel Garcia"])
briscoe = wc.createWrestler(wc.wrestleDictionary["Mark Briscoe"])
mox = wc.createWrestler(wc.wrestleDictionary["Jon Moxley"])
swerve = wc.createWrestler(wc.wrestleDictionary["Swerve Strickland"])
rush = wc.createWrestler(wc.wrestleDictionary["Rush"])
lethal = wc.createWrestler(wc.wrestleDictionary["Jay Lethal"])
white = wc.createWrestler(wc.wrestleDictionary["Jay White"])

blueLeague = wc.League([elIdolo, danielson, kingston, king, castagnoli, garcia])
goldLeague = wc.League([briscoe, mox, swerve, rush, lethal, white])

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

def point_totals():
    """
Automatically formats the league participants into neat and tidy stat blocks.\n
Mathematically-eliminated competitors are marked with strikethrough text.
    """
    print("Blue League:")
    for guy in blueLeague.roster:
        while len(guy.name) < 24:
            guy.name += " "
        if guy.losses >= 3:
            print("\u0336" + "\u0336".join(f"{guy.name}: {guy.points} points ({guy.wins}-{guy.losses}-{guy.draws})"))
        else:
            print(f"{guy.name}: {guy.points} points ({guy.wins}-{guy.losses}-{guy.draws})", f"TBPs: {guy.TBP}", sep = "|")
    print("\nGold League:")
    for dude in goldLeague.roster:
        while len(dude.name) < 24:
            dude.name += " "
        if dude.losses >= 3:
            print("\u0336" + "\u0336".join(f"{dude.name}: {dude.points} points ({dude.wins}-{dude.losses}-{dude.draws})"))
        else:
            print(f"{dude.name}: {dude.points} points ({dude.wins}-{dude.losses}-{dude.draws})", f"TBPs: {dude.TBP}", sep = "|")
