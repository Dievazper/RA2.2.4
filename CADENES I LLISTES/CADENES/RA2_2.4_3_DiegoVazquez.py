# Autor: Harry White
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció que reverteixi una cadena.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una cadena de text
# Especificacions de sortida
# Imprimeix la cadena invertida
cadena_original = input("Introdueix la cadena que vols revertir: ")
cadena_revertida = cadena_original[::-1]
print(f"Original: {cadena_original}")
print(f"Revertida: {cadena_revertida}")