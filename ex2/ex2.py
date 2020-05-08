import matplotlib.pyplot as plt
import random
import math
# Choisir la loi : 
# v.a.r X => "Nombre de lancé d'une pièce non truquée tombant sur face sur 10 lancés"

# Question 1
# L'espérance de Xbarre_N consiste à calculer l'espérance de la moyenne empirique.

# Experience sur 10 lancés, renvoie le nombre de face
def experience():
    i = 0
    cpt_f = 0
    # pour 10 lancés
    while i < 10:
        if random.randint(0,1) == 0 :
            cpt_f = cpt_f + 1
        i = i + 1
        
    return cpt_f    

def calculMoyenneExperience(arrE):
    return (sum(arrE) / len(arrE))

def calculEcartTypeExperience(arrE, m):
    # sum((x_i-xbarre)²)
    tmp = sum([ pow(x - m, 2) for x in arrE])
    s = math.sqrt(tmp/len(arrE))
    return s

# nbE nombre d'experience
def main():
    exp = []
    
    i = 0
    # pour 100 000
    while i < 100000:
        gen = experience()
        exp.append(gen)
        i = i + 1

# Pour éviter du lag sur la fenêtre ainsi qu'un temps de calcul elevé,
# nous avons décidé de ne pas afficher les points pour les expériences sur 100000 et 10000

    # Entier
    m1 = calculMoyenneExperience(exp) # Moyenne
    s1 = calculEcartTypeExperience(exp, m1) # Ecart-type
    print("Pour 100 000 experiences, m =",m1,"; s =",s1)

    # Calcul des "droites" de moyenne et de l'écart-type en + et -
    m_arr = [ m1 for x in exp] # Tableau moyenne
    s_arr_plus = [ m1 + s1 for x in exp] # Tableau écart-type en +
    s_arr_minus = [ m1 - s1 for x in exp] # Tableau écart-type en -

    plt.figure()
    plt.subplot(511)
    plt.title('Moyenne et ecart type en fonction de la loi X')
    plt.plot(m_arr, 'b', s_arr_plus, 'g--', s_arr_minus, 'g--')

    # 10 000
    exp2 = exp[0:10000]
    m2 = calculMoyenneExperience(exp2)     
    s2 = calculEcartTypeExperience(exp2, m2)
    print("Pour 10 000 experiences, m =",m2,"; s =",s2)
    m_arr = [ m2 for x in exp2]
    s_arr_plus = [ m2 + s2 for x in exp2]
    s_arr_minus = [ m2 - s2 for x in exp2]
    plt.subplot(512)
    plt.plot(m_arr, 'b', s_arr_plus, 'g--', s_arr_minus, 'g--')

    # 1 000
    exp3 = exp[0:1000]
    m3 = calculMoyenneExperience(exp3)     
    s3 = calculEcartTypeExperience(exp3, m3)
    print("Pour 1 000 experiences, m =",m3,"; s =",s3)
    m_arr = [ m3 for x in exp3]
    s_arr_plus = [ m3 + s3 for x in exp3]
    s_arr_minus = [ m3 - s3 for x in exp3]
    plt.subplot(513)
    plt.plot(exp3,'rx', m_arr, 'b', s_arr_plus, 'g--', s_arr_minus, 'g--')

    # 100
    exp4 = exp[0:100]
    m4 = calculMoyenneExperience(exp4)     
    s4 = calculEcartTypeExperience(exp4, m4)
    print("Pour 100 experiences, m =",m4,"; s =",s4)
    m_arr = [ m4 for x in exp4]
    s_arr_plus = [ m4 + s4 for x in exp4]
    s_arr_minus = [ m4 - s4 for x in exp4]
    plt.subplot(514)
    plt.plot(exp4,'rx', m_arr, 'b', s_arr_plus, 'g--', s_arr_minus, 'g--')

    # 10
    exp5 = exp[0:10]
    m5 = calculMoyenneExperience(exp5)     
    s5 = calculEcartTypeExperience(exp5, m5)
    print("Pour 10 experiences, m =",m5,"; s =",s5)
    print("Les 10 premiers éléments de la liste :",exp[1:10])
    m_arr = [ m5 for x in exp5]
    s_arr_plus = [ m5 + s5 for x in exp5]
    s_arr_minus = [ m5 - s5 for x in exp5]
    plt.subplot(515)
    plt.plot(exp5,'rx', m_arr, 'b', s_arr_plus, 'g--', s_arr_minus, 'g--')

    plt.show()
    plt.close()

main()


