# Autor: Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció que sumi tots els nombres d'una llista.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una llista de nombres separats per espais
# Especificacions de sortida
# Imprimeix la suma de tots els nombres de la llista
nombres = []

quantitat = int(input("Quants números vols sumar? "))

print(f"Introdueix {quantitat} números, un per un:")

for i in range(quantitat):
    num = int(input(f"Número {i+1}: "))
    nombres.append(num)

total = sum(nombres)

print(f"La llista que has introduït és: {nombres}")
print(f"La suma total és: {total}")