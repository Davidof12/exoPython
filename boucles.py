#depuis la bibliothèque random, on importe la formule (fonction) randrange ()
#qui permet de récuper un chiffre aléatoire
from random import randrange

#-----------------------------
#exemple 1

#on cree une variable qui contient lz chzine de caractere "Bonjour a tous!""
phrase = "Bonjour a tous !"

#for permet de parcourir la phrase en recuperant chaque caractere et la stoque temporairement dans "lettre"
for lettre in phrase:
        #on compare la lettre recupere avec la liste de voyelles
    if lettre in "aeiou":
        print(lettre)
        
#-----------------------------
#exemple 2
#input permet de demander quelqueque chose au clavier
#ici, un entier (int)  
#on stoque la valeur tapez dans table
table = int(input("tapez un chiffre : "))
multiple = 1
#tant que la variable multiple est plus petit ou egale a 10
while multiple <= 10:
    #on affiche la multiplication de la table choisie avec son multiplicateur
    print (table * multiple)
    #on augmente a chaque tour la variable multiple de +1
    multiple = multiple + 1



#-----------------------------
#exemple 3
#on demande a randrange de nous donner un chiffre aleatoire compris
#entre 0 et 99 puis on stoque le résultat dans chiffre
chiffre = random.randrange(100)

#on cree une variable booleenne trouver qui va vaut FAUX
trouver = False

#tant que trouver est egale a FAUX, on continue la boucle
while trouver == False :
    a = int(input("Entrez un chiffre : "))
    if a < chiffre:
        print("le chiffre est plus grand")
    elif a > chiffre:
        print("le chiffre est plus petit")
    else:
        print("Bravo !")
        #si on a trouve, il faut penser a changer la valeur de notre "Flag"
        # notre "Flag" trouver qui passe a VRAI
        trouver = True
