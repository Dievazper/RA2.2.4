# Autor:Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari 5 paraules i emmagatzema-les en una llista

# Especificacions d'entrada
# Demana a l'usuari que introdueixi 5 paraules
# Especificacions de sortida
# Imprimeix la llista de paraules introduïdes
paraules = []
print("Introdueix 5 paraules, una per una:")

for i in range(5):
    paraula = input(f"Paraula {i+1}: ")
    paraules.append(paraula)

print(f"La llista completa és: {paraules}")