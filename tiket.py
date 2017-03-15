"""
classes:
graph thing (adj list)
tickets
players (+ownership)
    can have their own adjlists
"""
from random import *
import TrainGraph as trains
import DestinationCards as dest

ee = trains.edges
no = trains.nodes
de = dest.dests

def pathinator(self, curr, adj, mask):
    ans = 0
    for i in range(len(adj[curr])):
        v = i[0]
        w = i[1]
        if bitmask[i] & (1 << v):
            bitmask = [x for x in mask]
            bitmask[i] &= ~(1 << v)
            bitmask[v] &= ~(1 << i)
            ans = max(ans, wt + pathinator(v, adj, bitmask))
    return ans


class UnionFind: #optimized with rank heuristics
	def __init__(self, size):
		self.parents = [i for i in range(size)]
        self.rank [0 for i in range(size)]

	def find(self, n):
		if self.parents[n] is -1:
			return n
		else:
			return self.find(self.parents[n])

	def same(self, x, y):
		return self.find(x) == self.find(y)

	def unify(self, x, y):
		if not self.same(x, y):
			a = self.find(x)
			b = self.find(y)
			if self.rank[a] <= self.rank[b]:
				self.parents[a] = b
				if self.rank[a] == self.rank[b]:
					self.rank[b] += 1
			else:
				self.parents[b] = a

class CardSet:
    def __init__(self, red=0, blue=0, green=0, black=0, orange=0, yellow=0, pink=0, wild=0): # i don't remember all the colors
        self.cards = [red, blue, green, black, orange, yellow, pink, wild]
        self.trans = {'r':0, 'blu':1, 'g':2, 'bla':3, 'o':4, 'y':5, 'p':6, 'w':7}

    def addCard(self, num, color):
        if isinstance(color, str):
            self.cards[self.trans[color]] += num
        else:
            self.cards[color] += num

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

class Deck:
    def __init__(self):
        self.up = []
        self.trans = {'r':0, 'blu':1, 'g':2, 'bla':3, 'o':4, 'y':5, 'p':6, 'whi': 7, 'wil':8}
        for i in range(4):
            self.addToDisp()

    def canAdd(self):
        return len(self.up) < 4

    def addToDisp(self):
        if self.canAdd():
            self.up.append(self.blindDraw())

    def fill(self):
        while self.canAdd():
            self.addToDisp()

    def blindDraw(self):
        return randint(0,8)

    def drawDisp(self, nums):
        if self.up[nums[0]] == 8 or (len(nums) == 2 and self.up[nums[1]] == 8):
            nums.pop()
        ans = []
        for i in nums:
            ans.append(self.up[i])
            self.up[i] = self.blindDraw()
        return ans

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = CardSet()
        self.goals = []
        self.trains = 45
        self.adj = [[] for i in range(36)]
        self.trans = {'r':0, 'blu':1, 'g':2, 'bla':3, 'o':4, 'y':5, 'p':6, 'whi': 7, 'wil':8}
        self.equivalence = [0, 1, 2, 4, 7, 10, 15]
        self.conn = UnionFind(36)

    def doubleDestinyDraw(self, deck):
        self.hand.addCard(1, deck.blindDraw())
        self.hand.addCard(1, deck.blindDraw())

    def doubleDisplay(self, deck, draws):
        res = deck.drawDisp(draws)
        for i in res:
            self.hand.addCard(1, i)

    def dispBlind(self, deck, draw):
        self.hand.addCard(1, deck.drawDisp(draw)[0])
        self.hand.addCard(1, deck.blindDraw())

    def wildDisp(self, deck, draw):
        deck.drawDisp(draw)
        self.hand.addCard(1, 'w')

    def claimTrack(self, track):
        i = self.track.node1
        j = self.track.node2
        w = self.track.weight
        c = self.track.color
        if self.hand.canBuy(w, c) and self.trains >= w:
            rem = w
            col = self.hand.cards[self.trans[c]]
            rem -= min(w, col)
            self.hand.addCard(-min(w, col), c)
            if rem > 0:
                self.hand.addCard(-rem, 'wil')
            if j not in self.adj[i]:
                self.adj[i].append((j, w))
            if i not in self.adj[j]:
                self.adj[j].append((i,w))
            self.trains -= w
            self.score += self.equivalence[w]
            self.conn.unify(i, j)

    def getGoal(self, goal):
        self.goals.append(goal)

    def pather(self):
        ans = -1
        for i in range(36):
            ans = max(ans, pathinator(i, self.adj, [(1 << len(j)) for j in range(self.adj)]))
        return ans

    def procGoals(self):
        for i in self.goals:
            if self.conn.same(i[0], i[1]):
                self.score += i[2]
            else:
                self.score -= i[2]

class Game:
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.players = [Player(input("Player " + (i+1) + " name: ")) for i in range(self.numPlayers)]
        self.inPlay = True
        self.goals = [i for i in de]
        shuffle(self.goals)
        self.deck = Deck()
        self.curr = 0
        self.tracks = [i for i in ee]
        self.actionTaken = False
        self.endgame = False
        self.endat = 100

        for i in self.players:
            for j in range(2):
                i.doubleDestinyDraw(self.deck())
            for j in range(3):
                self.dealGoal(i)

    def processTurn(self):
        p = self.players[self.curr]
        while not self.actionTaken:
            print("Actions:")
            print("[1] Draw cards.")
            print("[2] Buy a track.")
            print("[3] Pass.")
            com = int(input("Choose: "))
            if com < 1 and 2 < com:
                print("Invalid.")
                continue
            elif com == 1:
                print("Draw cards.")
                print("[1] Train Cards.")
                print("[2] Destination Cards.")
                com = int(input("Choose: "))
                if com == 1:
                    print("What kind of draw?")
                    print("[1] Double blind draw")
                    print("[2] Double face-up draw")
                    print("[3] 1 Face-up, 1 Blind")
                    if 8 in self.deck.up:
                        print("[4] Wild from face-up")
                    com = int(input("Choose: "))
                    if com == 1:
                        p.doubleDestinyDraw(self.deck)
                    elif com == 2:
                        drawSuccess = False
                        while not drawSuccess:
                            thing = list(set(map(int, input("Two locants for the cards you want (0 based)? No wilds, though: ").split())))
                            if len(thing) > 2:
                                thing = thing[:2]
                            if len(thing) < 2:
                                continue
                            if thing[0] < 0 or thing[0] > 3  or thing[1] < 0 or thing[1] > 3:
                                continue
                            if self.deck.up[thing[0]] == 8 or self.deck.up[thing[1]] == 8:
                                continue
                            p.doubleDisplay(self.deck, thing)
                            break
                    elif com == 4 and 8 in self.deck.up:
                        p.wildDisp(self.deck, self.deck.up.index(8))
                    else:
                        while True:
                            num = int(input("Locant of card to draw (0 based)? No wilds: "))
                            if num < 0 or num > 3:
                                continue
                            if self.deck.up[num] == 8:
                                continue
                            p.dispBlind(self.deck, num)
                            break
                else:
                    self.dealGoal(p)
                break
            elif com == 2:
                for k,v in no.items():
                    print(k,v)
                while True:
                    f = int(input("From what node #? "))
                    t = int(input("To what node #? "))
                    if f == t:
                        continue
                    if t > f:
                        f,t = t,f
                    trek = [i[0] for i in self.tracks if i[0].node1 == f and i[0].node2 == t and i[1] == 0]
                    if len(trek) == 0:
                        continue
                    idx = self.tracks.index([trek[0], 0])
                    self.tracks[idx][1] = 1
                    p.claimTrack(trek[0])
                break
            else:
                break
            self.curr += 1
            self.curr %= self.numPlayers
            if self.endgame and self.endat == self.curr:
                self.endGame()
            if p.trains < 3:
                self.endgame = True
                self.endat = self.curr

    def endGame(self): #fuck this
        for i in self.players:
            i.procGoals()
        idx = 0
        ans = 0
        for i in range(len(self.players)):
            tmp = self.players[i].pather
            if tmp > ans:
                ans = tmp
                idx = i
        self.players[idx].score += 10
        ans = 0
        for i in range(len(self.players)):
            tmp = self.players[i].score
            if tmp > ans:
                ans = tmp
                idx = i
        print("Player " + str(i+1) + " wins!")
        self.inPlay = False

    def dealGoal(self, player):
        thing = [self.goals.pop() for i in range(3)]
        p = player
        while True:
            nums = list(set(map(int, input("Indices of cards to keep?").split())))
            if len(nums) == 0:
                continue
            try:
                for i in nums:
                    p.getGoal(thing[i])
                for i in range(3):
                    if i not in nums:
                        self.goals.append(thing[i])
            except:
                continue
            break
