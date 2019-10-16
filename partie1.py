# ex 1 afficher "hello world"
print ("excercice 1")
print ("hello world")
Mahyadine = "hello world"
print(Mahyadine)

# ex 2 Calcul divers
print ("excercice 2")
print (3*3, 4+9+78, 12-7, 5e4)
try: 12/0
except:
    print ("impoosible de diviser par 0")
            

# ex 3 Communiquer avec l'ordinateur
print ("excercice 3")
choix=input ("Bonjour veuillez indiquer votre nom et prénom:")
print ("Bienvenue "+ choix)

# ex 4 Nom et prénom
print ("excercice 4")
nom = "Yassi"
prenom = "Mahyadine"
print ("Bonjour {} {}".format(nom,prenom))

# ex 5 Des caractères au nombre
print ("excercice 5")
mynumber = "123"
print (int(mynumber))

# ex 6 Majuscules et miniscules
print ("excercice 6")
mot=input ("Veuillez entrer votre texte ici")
print(mot.upper())
print(mot.lower())
