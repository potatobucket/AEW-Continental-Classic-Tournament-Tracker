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

blueLeagueMatches = [wc.Match(match[0], match[1]) for match in blueLeague.matches]
goldLeagueMatches = [wc.Match(match[0], match[1]) for match in goldLeague.matches]

def point_totals():
    print("Blue League:")
    for guy in blueLeague.roster:
        while len(guy.name) < 24:
            guy.name += " "
        if guy.losses >= 3:
            print("\u0336" + "\u0336".join(f"{guy.name}: {guy.points} points ({guy.wins}-{guy.losses}-{guy.draws})"))
        else:
            print(f"{guy.name}: {guy.points} points ({guy.wins}-{guy.losses}-{guy.draws})")
    print("\nGold League:")
    for dude in goldLeague.roster:
        while len(dude.name) < 24:
            dude.name += " "
        if dude.losses >= 3:
            print("\u0336" + "\u0336".join(f"{dude.name}: {dude.points} points ({dude.wins}-{dude.losses}-{dude.draws})"))
        else:
            print(f"{dude.name}: {dude.points} points ({dude.wins}-{dude.losses}-{dude.draws})")
