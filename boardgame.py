class BoardGame:
    def __init__(self, name, gibbonsrating, baverage, avgweight, yearpublished, bggbestplayers):
        self.name = name
        self.gibbonsrating = float(gibbonsrating)
        self.baverage = float(baverage)
        self.avgweight = float(avgweight)
        self.yearpublished = int(yearpublished)
        self.bggbestplayers = str(bggbestplayers).split(',')