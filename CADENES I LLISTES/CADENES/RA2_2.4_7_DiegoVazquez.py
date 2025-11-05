# Autor: Diego Vázquez
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana una cadena i compta quantes vegades apareix una lletra concreta.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una cadena de text i una lletra concreta
# Especificacions de sortida
# Imprimeix el nombre de vegades que la lletra apareix en la cadena

cadena = input("Introdueix la cadena: ")
lletra = input("Quina lletra vols comptar? ")

if len(lletra) == 1:
    comptador = cadena.lower().count(lletra.lower())
    print(f"La lletra '{lletra}' apareix {comptador} vegades (sense distinció maj./min.).")
else:
    print("Error: Has d'introduir només una lletra.")