
On cree une variable qui vaut 5
boite = 5

#On stock les elements
if boite > 10 :
    print("plus grand")

elif boite < 10 :
    print("plus petit")

else:
    print("egal")


#------------------
#exemple 2

#on garde le reste de la division de 52 par 2 (le modulo)

#On stock le résultat dans la variable boite
boite = 52 % 2

#si le contenu de la variable boite est egal a 0
#ATTENTION, double = quand on compare 2 elements
if boite == 0 :
    print("52 est un chiffre pair ")