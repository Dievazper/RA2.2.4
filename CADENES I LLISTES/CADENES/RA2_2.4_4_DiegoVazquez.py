# Autor: Diego Vázquez
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana una paraula i verifica si és un palíndrom.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una paraula
# Especificacions de sortida
# Indica si la paraula és un palíndrom o no
paraula = input("Introdueix una paraula per verificar si és un palíndrom: ")
paraula_neta = paraula.lower()
if paraula_neta == paraula_neta[::-1]:
    print(f"'{paraula}' SÍ que és un palíndrom.")
else:
    print(f"'{paraula}' NO és un palíndrom.")