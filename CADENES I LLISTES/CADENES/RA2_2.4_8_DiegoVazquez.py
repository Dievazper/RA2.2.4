# Autor: Diego Vázquez
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Escriu una funció que elimini tots els espais d'una cadena.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una cadena de text
# Especificacions de sortida
# Imprimeix la cadena sense espais
frase_amb_espais = input("Introdueix una frase per treure-li els espais: ")
frase_sense_espais = frase_amb_espais.replace(" ", "")

print(f"Original: '{frase_amb_espais}'")
print(f"Sense espais: '{frase_sense_espais}'")