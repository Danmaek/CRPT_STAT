# python 3.7.4

# écrire un programme du calcul des coefficients de Bezout
# https://www.youtube.com/watch?v=bWHY9Eto2wU
# https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide

# On recherche u et v tel que : pgcd(r0, r1) = u*r0 + v*r1

# PGCD Euclide, renvoit un tableau (format calcul PGCD)
# Le valeur du PGCD est en arr[0][2] conformément à la mise en forme calcul PGCD
def calculPGCD(a, b):
    #Initialisation
    arr = [[a, nfois(a,b), b, a%b]]
    return PGCD(arr)

# calcul du pgcd en récursif
def PGCD(arr):
    # a <- b
    a = arr[0][2]
    # b <- reste a%b
    b = arr[0][3]

    # si b == 0
    if b == 0 :
        lirePGCD(arr)
        return arr

    # insere le tableau de l'étape du calcul du pgcd
    else :
        arr.insert(0, [a, nfois(a,b), b, a%b])
        return PGCD(arr)

# nombre de fois qu'il est possible de possible de diviser a par b
def nfois(a, b):
    cpt = 0
    while(a - b >= 0 and b!=0):
        cpt = cpt + 1
        a = a - b
    return cpt

# lecture du tableau pgcd formaté
def lirePGCD(arr):
    for i in range(len(arr)):
        print(arr[i][0]," = ", arr[i][1], " * ", arr[i][2]," + ", arr[i][3])

# calcul des coefficients de bezout
def coeffBezout(x, y):
    pgcd_arr = calculPGCD(x,y)

    # test de la valeur du PGCD
    if(pgcd_arr[0][2] == 1):
        print("Les entier ", x, " et ", y, " sont premiers entre eux.")
    else:
        print("Les entier ", x, " et ", y, " ne sont pas premiers entre eux.")
        print('echec - fin coeffBezout')
        return -1

  # Initialisation r0, u, r1 et v
    u = 1
    a = pgcd_arr[1][0]
    v = - pgcd_arr[1][1]
    b = pgcd_arr[1][2]

    if(len(pgcd_arr) > 2):
        for i in range(2, len(pgcd_arr)):
            #décalage de r0
            tmp_u = v
            # décalage de a
            tmp_a = pgcd_arr[i][0]
            # on rassemble les facteurs du même nombre v
            tmp_v = u + (v * (-pgcd_arr[i][1]))
            # décalage de v
            tmp_b = pgcd_arr[i][2]

            # affectation au bv
            a = tmp_a
            u = tmp_u

            b = tmp_b
            v = tmp_v

    print("PGCD(",x, ",", y, ") =", a, "×", u, "+ (", b, "*", v,")")
    return [a,u,b,v]

# result = coeffBezout(71,131)
# print(result)