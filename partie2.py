# ex 1 afficher "True ou False"
print ("excercice 1")
un = ""
deux = "mahya"
print(len(un)==0)
print(len(deux)==0)


# ex 2 Calculer mon âge
print ("excercice 2")
annee=input ("Veuillez indiquer l'année en cours ? ") 
naissance=input ("Veuillez indiquer votre année de naissance ? ")
annee=int(annee)
naissance=int(naissance)
age =int(annee-naissance)
print ("Vous avez",age,"ans")
ageduvoisin=int(input("Quelle age à votre voisin ? "))
total = (age)+(ageduvoisin)
print("A vous deux vous avez",total,"ans")

# ex 3 Problème de chaussures
print ("excercice 3")
chaussures = 70
jean = 59
tshirt = 20
total = chaussures + jean + tshirt
print ("Le total de vos achats est de {} euro avec la reduction de 20%".format(total*0.8)) #ici on met le .format pour gagner une ligne

# ex 4 une calculatrice Python
print ("excercice 4")
nombre1=input ("veuillez entrée la première valeur ")
nombre2=input ("veuiller entrée la deuxième valeur ")
print (float(nombre1)+float(nombre2))

# ex 5 travailler avec les propriétés
print ("exercice 5")
prenom=input ("veuillez entrer votre prénom ").upper()
nom=input ("veuillez entrer votre nom ").upper()
print (prenom[0] + prenom[-1])
print (nom[0] + nom[-1])
n= (prenom[0] + prenom[-1]) + (nom[0] + nom[-1])
print (n)
age= int( input ("veuillez entrer votre age "))
division = round(age/33)
print ("Votre age est de {} ans .".format(division))

