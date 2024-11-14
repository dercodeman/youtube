# Zinsenfalle bei Schulden und Hauskredit berechnen und verstehen

meineSchuld = 500000
zins = 0.04 # p.a. - per annum - pro Jahr
# Jahre unbekannt
abzahlen = 2000 # pro Monat

BK = [meineSchuld] # BK[0] = meineSchuld, BK[1] = noch unbekannt...
BKZF = [meineSchuld] # zinsfrei
# "while"-Schleife
j = 0
while BK[j] > 0:
	# Die Idee ist einfach eine zweite Liste zu haben die ohne Zinsen schrumpft
	# Und von dieser Liste BKZF berechnen wir die Zinsen für BK
	temp1 = BK[j] - abzahlen*12 + BKZF[j]*zins
	temp2 = BKZF[j] - abzahlen*12
	BK.append(temp1)
	
	# Damit wir keine negativen Werte auf die zinslose Liste addieren
	# benutze ich eine if-Anweisung um es durch eine 0 zu ersetzen.
	# Andernfalls zahlt man plötzlich negative Zinsen!
	if temp2 > 0:
		BKZF.append(temp2)
	else:
		BKZF.append(0)
		
	print(f"Jahr: {2025+j} | {j:2} | Meine Schuld: {BK[j]:.2f} Euro")
	j += 1
	
abgezahlt = 12 * abzahlen * j + BK[j]
print("-----------------------------------------------")
print(f"{'Schulden: ':25} {meineSchuld:.2f} Euro")
print(f"{'Insgesamt abbezahlt: ':25} {abgezahlt:.2f} Euro\n")
print(f"{'Gesamtzins: ':25} {(abgezahlt/meineSchuld-1)*100:.0f} %")