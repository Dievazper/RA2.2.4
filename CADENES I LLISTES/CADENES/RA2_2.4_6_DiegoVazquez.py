# Autor: Diego Vázquez
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana una cadena i mostra la primera i l'última lletra.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una cadena de text
# Especificacions de sortida
# Imprimeix la primera i l'última lletra de la cadena
cadena = input("Introdueix una cadena: ")

if len(cadena) > 0:
    print(f"Primera lletra: {cadena[0]}")
    print(f"Última lletra: {cadena[-1]}")
else:
    print("La cadena és buida, no té primera ni última lletra.")