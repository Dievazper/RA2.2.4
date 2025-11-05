# Autor: Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi 10 números
# Especificacions de sortida
# Imprimeix les dues llistes: una amb els números parells i una altra amb els números senars
parells = []
senars = []

print("Introdueix 10 números:")

for i in range(10):
    num = int(input(f"Número {i + 1}: "))
    if num % 2 == 0:
        parells.append(num)
    else:
        senars.append(num)

print(f"Números parells: {parells}")
print(f"Números senars: {senars}")