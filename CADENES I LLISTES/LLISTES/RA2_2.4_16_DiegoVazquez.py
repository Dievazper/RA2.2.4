# Autor: Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Fes un programa que elimini els duplicats d'una llista.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una llista de nombres separats per espais
# Especificacions de sortida
# Imprimeix la llista sense duplicats
llista_amb_duplicats = []
quantitat = int(input("Quants elements vols introduir a la llista? "))

print("Introdueix els elements (poden ser paraules o números):")
for i in range(quantitat):
    element = input(f"Element {i + 1}: ")
    llista_amb_duplicats.append(element)
llista_sense_duplicats = list(set(llista_amb_duplicats))

print(f"Llista original: {llista_amb_duplicats}")
print(f"Llista sense duplicats: {llista_sense_duplicats}")