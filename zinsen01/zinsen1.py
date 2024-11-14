# Zinsen und Zinseszins auf dem Sparbuch berechnen

## Matheformel: meinGeld * (1 + zinsen) ** jahre

meinGeld = 20000
zins = 0.03
jahre = 10

# Variante 1 (kurz, "magisch" / mathematisch hergeleitet)
Bankkonto = meinGeld*(1+zins)**jahre

# Variante 2 (ausführlich)
# Pro: Weniger Mathematik-Zauber
# Contra: Mehr Programmierverständnis nötig -> gutes Training
BK = [meinGeld,0,0,0,0,0,0,0,0,0,0] # BK[0] = meinGeld, BK[1] = 0, ...

# "for"-Schleife
for x in [1,2,3,4,5,6,7,8,9,10]:
	BK[x] = BK[x-1] + BK[x-1]*zins # meinGeld + meinGeld*Zins
	print(f"Jahr: {2024+x} | Geld: {BK[x]:.2f} Euro")

