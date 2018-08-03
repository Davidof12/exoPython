

choix = int(input("Tapez 1 pour C->F et 2 pour F->C"))

#...on converti des celsius en farenheit
if choix == 1:
    #---- 
    c= int(input("Tapez une temperature en C°"))
    farenheit = (c*1.8)+32 #formule c'est la trouver sur Google
    print(farenheit)

elif choix == 2:
    #...on converti des farenheit en celsius
    #---- 
    f= int(input("Tapez une temperature en F°"))
    celcius = (f-32)/1.8
    print(celcius)