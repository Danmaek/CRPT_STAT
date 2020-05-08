# python 3.7.4
import math
import random
from expo_rapide import exponentiation_rapide
from identite_bezout import coeffBezout
from decimal import Decimal 

# écrire un programme de chiffrement RSA
# https://fr.wikipedia.org/wiki/Chiffrement_RSA

def cles(p,q) :
    # Calcul du module de chiffrement 
    n = p * q
    print("n =",n)
    
    # Calcul de phi(n), indicatrice d'Euler en n
    phi_n = (p - 1) * (q - 1)
    
    # Formule prévisible car parcourt incrémental (pour réduire le temps de calcul nécessaire)
    for e in range(2, phi_n - 1) :
        if estPremier(e, phi_n) == 1 :
            break
    
    # # Formule aléatoire
    # for e in random.randrange(2, phi_n):        
    #     if estPremier(e, phi_n):
    #         break

    # Formule avec calcul des coefficients de Bezout
    arr = []
    arr_bezout = coeffBezout(e,phi_n)
    print("e,",e,"  phi_n",phi_n)
    print(arr_bezout)
    d = arr_bezout[1]
    # On rajoute la valeur du modulo 1 fois si d est négatif
    # a * d = 1 [r1]
    if d < 0 : 
        d = d + phi_n

    # # Formule sans coefficient de Bezout
    # Ici on a : [a * d + b * v = 1] <= on trouve => 
    # On cherche un u à la seconde expression
    # for d in range(1, phi_n - 1):
    #     un = (e * d) % phi_n 
    #     if un == 1 : 
    #         break

    cle_public = [e, n]
    cle_privee = [d, n]
    arr = [cle_public, cle_privee]
    print(arr)
    return arr

# Renvoie a = 1 si a et b sont premier
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

    # Chiffrement avec le couple
    encrypted_msg_bytes = []
    for char in text:
        byte = 0 if char == " " else ord(char) - 96
        encrypted_msg_bytes.append(exponentiation_rapide(byte if char == " " else ord(char) - 96, cle_public[0]) %  cle_public[1])

    # Vérification : déchiffrement des valeurs
    decrypted_msg_chars = []
    for byte in encrypted_msg_bytes:
        decrypted_byte = exponentiation_rapide(byte, cle_privee[0]) % cle_privee[1] 
        decrypted_msg_chars.append(" " if decrypted_byte == 0 else chr(decrypted_byte + 96))

    print("message",text)
    print("encrypted", encrypted_msg_bytes)
    print("decrypted", decrypted_msg_chars)


RSA()

# Utiliser le couple (p q) = (71 131)// son premier entre eux
# La première valeur de e trouvé sera 3 et sera utilisé
# La clé publique doit correspondre à (e, n) = (3, 9301)
# La clé privée doit correspondre à (d , n) = (6067, 9301)