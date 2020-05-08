# python 3.7.4

# écrire un programme d’exponentiation rapide
# https://fr.wikipedia.org/wiki/Exponentiation_rapide
def exponentiation_rapide(x, n):
    # Initialisation des variables internes
    x_ = 0
    n_ = 0

    # On initialise la remontée du code récursif
    if n == 1 :
        print("[", x,",", n,"] --> Résultat avant remonté ", x,".")
        return x

    # Cas n est pair
    # x^n = (x²)^(n/2)
    elif n%2 == 0 :
        x_ = x * x
        n_ = n / 2
        return exponentiation_rapide(x_,n_)
    
    # Cas n est impair
    # x^n = x*(x²)^((n-1)/2)
    else :
        x_ = x * x
        n_ = (n - 1)/2
        return x * exponentiation_rapide(x_,n_)

print("Test exponentiation rapide avec les valeur 2 et 8")
print("Résultat : ", exponentiation_rapide(2,8))
