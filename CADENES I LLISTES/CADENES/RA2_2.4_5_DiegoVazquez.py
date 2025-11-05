# Autor: Diego Vázquez
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Substitueix totes les lletres "a" per "@" en una frase donada.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una frase
# Especificacions de sortida
# Imprimeix la frase amb les substitucions realitzades
frase_donada = input("Introdueix una frase: ")
nova_frase = frase_donada.replace("a", "@").replace("A", "@")

print(f"Original: {frase_donada}")
print(f"Modificada: {nova_frase}")