def PGCD (m,n) :
	if m <= 0 or n <= 0 : raise Exception("impossible de calculer le PGCD")
	if m == 1 or n == 1 : return 1
	if m == n : return m
	if m < n : return PGCD(m, n-m)
	return PGCD(n, m-n)

# http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/expose_vigenere.html
def Guess_Key_Lenght(ciphertext,mot = 3):
	al = "".join([chr(97+i) for i in range(0,26)])
	al = al.upper()

	dico = {}
	for i in range (0, len (ciphertext)-2) :
		t = ciphertext [i:i+mot]
		if t in dico : dico [t].append (i)
		else : dico [t] = [i]

	dis = []
	for d in dico :
		p = dico [d]
		if len (p) > 1 :
			for i in range (0, len (p)-1) :
				dis.append(p[i+1]-p[i])

	if len (dis) == 0 : 
		return -1
	if len (dis) == 1 : return dis [0]

	longueur = PGCD (dis [0], dis [1])
	for d in dis :
		longueur = PGCD (longueur, d)

	if longueur > 5 :
		return longueur
	else :
		return Guess_Key_Lenght(ciphertext, mot+1)