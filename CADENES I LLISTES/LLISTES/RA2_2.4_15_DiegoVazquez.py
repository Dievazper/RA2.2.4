# Autor: Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari una llista de noms i elsS ordena alfabèticament.

# Especificacions d'entrada
# Especificacions de sortida
noms = []
quantitat = int(input("Quants noms vols introduir? "))

for i in range(quantitat):
    nom = input(f"Introdueix el nom {i + 1}: ")
    noms.append(nom)
noms.sort()

print(f"Noms ordenats alfabèticament: {noms}")