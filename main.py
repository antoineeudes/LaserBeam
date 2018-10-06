from ray import *

G = Grid(26, 26)

####################################################
### Pour creer un miroir '/' à la position 'A-A', utiliser set_mirror('A', 'A')
### Pour creer un miroir '\' à la position 'A-A', utiliser set_backmirror('A', 'A')
####################################################

G.set_backmirror('A', 'C')
G.set_mirror('C', 'C')
G.set_mirror('C', 'B')
G.set_mirror('E', 'F')
G.set_backmirror('E', 'B')
G.set_mirror('C', 'F')
G.set_backmirror('C', 'K')
G.set_backmirror('I', 'K')
G.set_backmirror('I', 'T')
G.set_mirror('L', 'T')
G.set_backmirror('L', 'G')
G.set_mirror('G', 'G')
G.set_mirror('G', 'X')
G.set_backmirror('C', 'X')
G.set_mirror('C', 'P')
G.set_mirror('Q', 'P')
G.set_mirror('Q', 'C')
G.set_backmirror('T', 'C')
G.set_mirror('T', 'W')
G.set_backmirror('R', 'W')
G.set_mirror('R', 'S')
G.set_backmirror('Y', 'S')

print(G)
c0, c1 = simulate_ray(G, 'A', '>')
print('\n')
print(G)

print("point de sortie : " + c0 + "-" + c1)
