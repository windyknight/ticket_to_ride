from enum import Enum

class Edge:
    def __init__(self, node1, node2, weight, color):
        self.node1 = node1;
        self.node2 = node2;
        self.weight = weight;
        self.color = color;
#
# class Node:
#     def __init__(self, name):
#         self.name = name;

nodes = {0: "Vancouver", 1: "Calgary", 2: "Winnipeg", 3 : "Sault St. Marie", 4: "Montreal",
         5 : "Seattle", 6 : "Helena", 7: "Duluth", 8: "Toronto",9: "Boston",
         10: "Portland", 11: "Omaha", 12: "Chicago", 13: "Pittsburg", 14: "New York",
         15 : "San Francisco", 16: "Salt Lake City", 17: "Denver", 18: "Kansas City", 19: "Saint Louis",
         20: "Los Angeles", 21: "Las Vegas", 22: "Phoenix", 23: "Santa Fe", 24: "Oklahoma City",
         25: "Little Rock", 26: "Nashville", 27: "Raleigh", 28: "Washington",
         29: "El Paso", 30: "Dallas", 31: "Houston", 32: "New Orleans", 33: "Atlanta", 34: "Charleston",
         35: "Miami"}

#Node 1 is always less than Node 2
#Edges of Vancouver
A = [Edge(0, 5, 1, None), 0]
B = [Edge(0, 5, 1, None), 0]
C = [Edge(0, 1, 3, None), 0]

#Edges of Calgary
D = [Edge(1, 5, 4, None), 0]
E = [Edge(1, 6, 4, None), 0]
F = [Edge(1, 2, 6, "whi"), 0]

#Edges of Winnipeg
G = [Edge(2, 6, 4, "blu"), 0]
H = [Edge(2, 7, 4, "bla"), 0]
I = [Edge(2, 3, 6, None), 0]

#Edges of Sault St. Marie
J = [Edge(3, 7, 3, None), 0]
K = [Edge(3, 8, 2, None), 0]
L = [Edge(3, 4, 5, "blah"), 0]

#Edges of Montreal
M = [Edge(4, 8, 3, None), 0]
N = [Edge(4, 14, 3, "blu"), 0]
O = [Edge(4, 9, 2, None), 0]
P = [Edge(4, 9, 2, None), 0]

#Edges of Seattle
Q = [Edge(5, 10, 1, None), 0]
R = [Edge(5, 10, 1, None), 0]
S = [Edge(5, 6, 6, "y"), 0]

#Edges of Helena
T = [Edge(6, 16, 3, "p"), 0]
U = [Edge(6, 17, 4, "g"), 0]
V = [Edge(6, 11, 5, "r"), 0]
W = [Edge(6, 7, 6, "o"), 0]

#Edges of Duluth
X = [Edge(7, 11, 2, None), 0]
Y = [Edge(7, 11, 2, None), 0]
Z = [Edge(7, 12, 3, "r"), 0]
AA = [Edge(7, 8, 6, "p"), 0]

#Edges of Toronto
BB = [Edge(8, 12, 4, "whi"), 0]
CC = [Edge(8, 13, 2, None), 0]

#Edges of Boston
DD = [Edge(9, 14, 2, "y"), 0]
EE = [Edge(9, 14, 2, "r"), 0]

#Edges of Portland
FF = [Edge(10, 15, 5, "g"), 0]
GG = [Edge(10, 15, 5, "p"), 0]
HH = [Edge(10, 16, 6, "b"), 0]

#Edges of Omaha
II = [Edge(11, 17, 4, "p"), 0]
JJ = [Edge(11, 18, 1, None), 0]
KK = [Edge(11, 18, 1, None), 0]
LL = [Edge(11, 12, 4, "b"), 0]

#Edges of Chicago
MM = [Edge(12, 19, 2, "g"), 0]
OO = [Edge(12, 19, 2, "w"), 0]
PP = [Edge(12, 13, 3, "o"), 0]
QQ = [Edge(12, 13, 3, "bla"), 0]

#Edges of Pittsburg
RR = [Edge(13, 19, 5, "g"), 0]
SS = [Edge(13, 26, 4, "y"), 0]
TT = [Edge(13, 27, 2, None), 0]
UU = [Edge(13, 28, 2, None), 0]
VV = [Edge(13, 14, 2, "whi"), 0]
WW = [Edge(13, 14, 2, "g"), 0]

#Edges of New York
XX = [Edge(14, 28, 2, "o"), 0]
YY = [Edge(14, 28, 2, "bla"), 0]

#Edges of San Francisco
ZZ = [Edge(15, 16, 5, "o"), 0]
AAA = [Edge(15, 16, 5, "whi"), 0]
BBB = [Edge(15, 20, 3, "y"), 0]
CCC = [Edge(15, 20, 3, "p"), 0]

#Edges of Salt Lake City
DDD = [Edge(16, 21, 3, "o"), 0]
EEE = [Edge(16, 17, 3, "r"), 0]
FFF = [Edge(16, 17, 3, "y"), 0]

#Edges of Denver
GGG = [Edge(17, 22, 5, "w"), 0]
HHH = [Edge(17, 23, 2, None), 0]
III = [Edge(17, 24, 4, "r"), 0]
JJJ = [Edge(17, 18, 4, "bla"), 0]
KKK = [Edge(17, 18, 4, "o"), 0]

#Edges of Kansas City
LLL = [Edge(18, 24, 2, None), 0]
MMM = [Edge(18, 24, 2, None), 0]
NNN = [Edge(18, 19, 2, "blu"), 0]
OOO = [Edge(18, 19, 2, "p"), 0]

#Edges of Saint Louis
PPP = [Edge(19, 25, 2, None), 0]
QQQ = [Edge(19, 26, 2, None), 0]

#Edges of Los Angeles
RRR = [Edge(20, 21, 2, None), 0]
SSS = [Edge(20, 22, 3, None), 0]
TTT = [Edge(20, 29, 6, "bla"), 0]

#Edges of Phoenix
UUU = [Edge(22, 23, 3, None), 0]
VVV = [Edge(22, 29, 3, None), 0]

#Edges of Santa Fe
WWW = [Edge(23, 29, 2, None), 0]
XXX = [Edge(23, 24, 3, "blu"), 0]

#Edges of Oklahoma City
YYY = [Edge(24, 29, 5, "y"), 0]
ZZZ = [Edge(24, 30, 2, None), 0]
AAAA = [Edge(24, 30, 2, None), 0]
BBBB = [Edge(24, 25, 2, None), 0]

#Edges of Little Rock
CCCC = [Edge(25, 30, 2, None), 0]
DDDD = [Edge(25, 32, 3, "g"), 0]
EEEE = [Edge(25, 26, 3, "w"), 0]

#Edges of Nashville
FFFF = [Edge(26, 33, 1, None), 0]
GGGG = [Edge(26, 27, 3, "bla"), 0]

#Edges of Raleigh
HHHH = [Edge(27, 33, 2, None), 0]
IIII = [Edge(27, 33, 2, None), 0]
JJJJ = [Edge(27, 34, 2, None), 0]
KKKK = [Edge(27, 28, 2, None), 0]
LLLL = [Edge(27, 28, 2, None), 0]

#Edges of El Paso
MMMM = [Edge(29, 30, 4, "r"), 0]
NNNN = [Edge(29, 31, 6, "g"), 0]

#Edges of Dallas
OOOO = [Edge(30, 31, 1, None), 0]
PPPP = [Edge(30, 31, 1, None), 0]

#Edges of Houston
QQQQ = [Edge(31, 32, 2, None), 0]

#Edges of New Orleans
RRRR = [Edge(32, 33, 4, "y"), 0]
SSSS = [Edge(32, 33, 4, "o"), 0]
TTTT = [Edge(32, 35, 6, "r"), 0]

nodes = {0: "Vancouver", 1: "Calgary", 2: "Winnipeg", 3 : "Sault St. Marie", 4: "Montreal",
         5 : "Seattle", 6 : "Helena", 7: "Duluth", 8: "Toronto",9: "Boston",
         10: "Portland", 11: "Omaha", 12: "Chicago", 13: "Pittsburg", 14: "New York",
         15 : "San Francisco", 16: "Salt Lake City", 17: "Denver", 18: "Kansas City", 19: "Saint Louis",
         20: "Los Angeles", 21: "Las Vegas", 22: "Phoenix", 23: "Santa Fe", 24: "Oklahoma City",
         25: "Little Rock", 26: "Nashville", 27: "Raleigh", 28: "Washington",
         29: "El Paso", 30: "Dallas", 31: "Houston", 32: "New Orleans", 33: "Atlanta", 34: "Charleston",
         35: "Miami"}
#Edges of Atlanta
UUUU = [Edge(33, 35, 5, "blu"), 0]
VVVV = [Edge(33, 24, 2, None), 0]

#Edges of Charleston
WWWW = [Edge(34, 35, 4, "p"), 0]

edges = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL,MM,OO,PP,QQ,RR,SS,TT,UU,VV,WW,XX,YY,ZZ,AAA,BBB,CCC,DDD,EEE,FFF,GGG,HHH,III,JJJ,KKK,LLL,MMM,NNN,OOO,PPP,QQQ,RRR,SSS,TTT,UUU,VVV,WWW,XXX,YYY,ZZZ,AAAA,BBBB,CCCC,DDDD,EEEE,FFFF,GGGG,HHHH,IIII,JJJJ,KKKK,LLLL,MMMM,NNNN,OOOO,PPPP,QQQQ,RRRR,SSSS,TTTT,UUUU,VVVV,WWWW]
