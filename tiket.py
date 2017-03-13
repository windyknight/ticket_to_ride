"""
classes:
graph thing (adj list)
tickets
players (+ownership)
    can have their own adjlists
"""
class Track:
    lenToPts = [0,1,2,4,7,10,15]
    def __init__(self, isDouble, color, length): #to be upd8ed
        self.owners = []
        self.isDouble = isDouble
        self.color = color
        self.length = length
        self.pts = lenToPts[self.length]

    def full(self):
        return len(self.owner) == self.maxOwners


class TrainGraph:
    #we like trains
    stations =  {0: "Vancouver", 1: "Calgary", 2: "Winnipeg", 3 : "Sault St. Marie", 4: "Montreal",
                 5: "Seattle", 6: "Helena", 7: "Duluth", 8: "Toronto",9: "Boston",
                10: "Portland", 11: "Omaha", 12: "Chicago", 13: "Pittsburg", 14: "New York",
                15: "San Francisco", 16: "Salt Lake City", 17: "Denver", 18: "Kansas City", 19: "Saint Louis",
                20: "Los Angeles", 21: "Las Vegas", 22: "Phoenix", 23: "Santa Fe", 24: "Oklahoma City",
                25: "Little Rock", 26: "Nashville", 27: "Raleigh", 28: "Washington",
                29: "El Paso", 30: "Dallas", 31: "Houston", 32: "New Orleans", 33: "Atlanta", 34: "Charleston",
                35: "Miami"} # the place where num : place is kept
    trans = {v:k for k,v in stations.items()} # reverse correspondence
    def __init__(self):
        self.adj = [[] for i in stations]


class CardSet:
    def __init__(self, red=0, blue=0, green=0, black=0, orange=0, pink=0, white=0, yellow=0, wild=0):
        self.cards = [red, blue, green, black, orange, pink, white, yellow, wild]
        self.trans = {'r':0, 'bu':1, 'g':2, 'bl':3, 'o':4, 'p':5, 'wt':6, 'y':7, 'wd':8}

    def addCard(self, num, color):
        self.cards[self.trans[color]] += num

    def canBuy(self, num, color):
        """
        Can you buy a thing given cost?
        """
        if color is None:
            for i in self.cards:
                if i >= num: return true
            return False
        else:
            color = self.trans[color]
            return self.cards[color] + self.cards[self.trans['w']] >= num

class Game:
    #don't know what Jay's gonna do with the destinations tbh, like will you make a class like track or meh?
    #i'll just leave it here
    allDestinations = [((0,4),20), ((0,23),13), ((1,16),7), ((1,22),13), ((2,25),11), ((2,31),12),
                       ((3,24),9), ((3,26),8), ((4,32),13), ((4,33),9), ((5,14),22), ((5,20),9),
                       ((6,20),8), ((7,29),10), ((7,31),8), ((8,35),10), ((9,35),12), ((10,22),11),
                       ((10,26),17), ((12,20),16), ((12,23),9), ((12,32),7), ((13,17),11), ((14,20),21),
                       ((14,30),11), ((14,33),6), ((15,33),17),  ((17,29),4), ((18,31),5), ((20,35),20)]
    def __init__(self, numPlayers, players):
        self.numPlayers = numPlayers
        self.players = players
        self.willEnd = False
        self.destinations = allDestinations
        self.faceDownDeck = CardSet(12, 12, 12, 12, 12, 12, 12, 12, 14)
        self.openFaceDeck = []
        self.currentPlayer = 0
        self.actionTaken = False
        self.trainGraph = TrainGraph()
        
class Player:
    def  __init__(self, index, name = "doodoo head", numTrains = 45):
        self.name = name
        self.score = 0
        self.index = index
        self.cardSet = cardSet()
        self.destinations = []
        self.numTrains = numTrains
        self.ownedTracks = []
    
    def claimTrack(track):
        if not track.full():
            ownedTracks.append(track)
            score.add(track.pts)
            
    def addCards(cs):
        self.cardSet += cs #DO OVERRIDING
