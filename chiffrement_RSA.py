# python 3.7.4
import math
import random
from identite_bezout import coeffBezout
from decimal import Decimal 

# écrire un programme de chiffrement RSA
# https://fr.wikipedia.org/wiki/Chiffrement_RSA


# L'étape de création des clés est à la charge d'Alice. Elle n'intervient pas à chaque chiffrement car les clés peuvent être réutilisées. La difficulté première, que ne règle pas le chiffrement, est que Bob soit bien certain que la clé publique qu'il détient est celle d'Alice. Le renouvellement des clés n'intervient que si la clé privée est compromise, ou par précaution au bout d'un certain temps (qui peut se compter en années).

# Choisir p et q, deux nombres premiers distincts ;
# calculer leur produit n = pq, appelé module de chiffrement ;
# calculer φ(n) = (p - 1)(q - 1) (c'est la valeur de l'indicatrice d'Euler en n) ;
# choisir un entier naturel e premier avec φ(n) et strictement inférieur à φ(n), appelé exposant de chiffrement ;
# calculer l'entier naturel d, inverse de e modulo φ(n), et strictement inférieur à φ(n), appelé exposant de déchiffrement ; d peut se calculer efficacement par l'algorithme d'Euclide étendu.
# Comme e est premier avec φ(n), d'après le théorème de Bachet-Bézout il existe deux entiers d et k tels que ed = 1 + kφ(n), c'est-à-dire que ed ≡ 1 (mod φ(n)) : e est bien inversible modulo φ(n).

# Le couple (n, e) — ou (e, n)3 — est la clé publique du chiffrement, alors que sa clé privée est4 le nombre d, sachant que l'opération de déchiffrement ne demande que la clef privée d et l'entier n, connu par la clé publique (la clé privée est parfois aussi définie comme le couple (d, n)3 ou le triplet (p, q, d)5).

def cles(p,q) :
    # Calcul du module de chiffrement 
    n = p * q
    print("n =",n)
    
    # Calcul de phi(n), indicatrice d'Euler en n
    phi_n = (p - 1) * (q - 1)
    
    # Choix de l'exposant de chiffrement e, entier naturel premier à phi(n) et < à phi(n)
    # pour la suite, il faut que e et phi_n soit premier
    # valeur d'initialisation
    
    for e in range(2, phi_n - 1) :
        if estPremier(e, phi_n) == 1 :
            break
    
    # *------------------INUTILE ----------------------------------------
    # Calcul de l'exposant de déchiffrement d, entier naturel inverse de e % phi(n) inférieur à phi(n)
    # par l'algorithme d'euclide étendu
    # arr_bezout = coeffBezout(e,phi_n)

    # a = arr_bezout[0] # correspond à e
    # b = arr_bezout[2] # correspond à phi_n
    # *----------------------------------------------------------

    # TODO
    # ici on a : [a * d + b * v = 1] <= on trouve => a * d = 1 [r1]
    # on cherche un u à la seconde expression
    for d in range(1, phi_n - 1):
        un = (e * d) % phi_n 
        if un == 1 : 
            break

    cle_public = [e, n]
    cle_privee = [d, n]
    arr = [cle_public, cle_privee]
    print(arr)
    return arr

# renvoie a = 1 si a et b sont premier
def estPremier(a, b):
    while (a != b):
        if a > b:
            a = a - b
        else :
            b = b - a
    return a

def RSA():
    p = int(input('Enter the value of p (natural integer) = ')) 
    q = int(input('Enter the value of p (natural integer) = ')) 
    text = str(input('Enter the value of the text (natural integer) = ')) 

    couple_cles = cles(p, q)
    cle_public = couple_cles[0]
    cle_privee = couple_cles[1]
    print("Cles publics " + str(cle_public))
    print("Cles privees " + str(cle_privee))

    # transformation du texte en list
    L = list(text)
    Lchiffre = []
    Lenint = []

    for i in range(0,len(L)) :
        # chiffrement avec le couple
        ctt = Decimal(0) 
        ctt = pow(ord(L[i]),cle_public[0]) 
        ct = ctt % cle_public[1] 

        Lenint.append(ord(L[i]))
        Lchiffre.append(ct)
    

    # vérification : déchiffrement des valeurs

    
    Ldechiffre = []
    Ldecint = []
    for i in range(0,len(Lchiffre)):
        dtt = Decimal(0) 
        dtt = pow(Lchiffre[i],cle_privee[0]) 
        dt = dtt % cle_privee[1]

        Ldecint.append(dt)
        Ldechiffre.append(chr(dt) )

    print(L)
    print(Lenint)
    print(Lchiffre)
    print(Ldecint)
    print(Ldechiffre)

RSA()

# utiliser le couple (p q) = (71 131) 13,21// son premier entre eux
# la première valeur de e trouvé sera 3 et sera utilisé
# la clé publique doit correspondre à (e, n) = (3, 9301)
# la clé privée doit correspondre à (d , n) = (6067, 9301)

# 75, 85