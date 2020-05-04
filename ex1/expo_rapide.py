# python 3.7.4

# écrire un programme d’exponentiation rapide
# https://fr.wikipedia.org/wiki/Exponentiation_rapide
def exponentiation_rapide(x, n):
    x_ = 0
    n_ = 0

    # On initialise la remontée du code récursif
    if n == 1 :
        print("[", x,",", n,"] --> Résultat avant remonté ", x,".")
        return x

    # x^n = (x²)^(n/2)
    elif n%2 == 0 :
        print(n, " est pair.")
        x_ = x * x
        n_ = n / 2
        return exponentiation_rapide(x_,n_)
    
    # x^n = x*(x²)^((n-1)/2)
    else :
        print(n, " est impair.")
        print("On garde ", x," pour la remontée.")
        x_ = x * x
        n_ = (n - 1)/2
        return x * exponentiation_rapide(x_,n_)


print("Solution : ", exponentiation_rapide(2,8))
