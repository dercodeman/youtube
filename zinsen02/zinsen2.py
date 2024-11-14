# Zinsenfalle bei Schulden und Hauskredit berechnen und verstehen

meineSchuld = 500000
zins = 0.04 # p.a. - per annum - pro Jahr
# Jahre unbekannt
abzahlen = 2500 # pro Monat

BK = [meineSchuld] # BK[0] = meineSchuld, BK[1] = noch unbekannt...

# "while"-Schleife
j = 0
while BK[j] > 0:
	temp = BK[j] - abzahlen*12 + BK[j]*zins
	BK.append(temp)
	print(f"Jahr: {2025+j} | {j:2} | Meine Schuld: {BK[j]:.2f} Euro")
	j += 1
	
abgezahlt = 12 * abzahlen * j + BK[j]
print("-----------------------------------------------")
print(f"{'Schulden: ':25} {meineSchuld:.2f} Euro")
print(f"{'Insgesamt abbezahlt: ':25} {abgezahlt:.2f} Euro\n")
print(f"{'Gesamtzins: ':25} {(abgezahlt/meineSchuld-1)*100:.0f} %")