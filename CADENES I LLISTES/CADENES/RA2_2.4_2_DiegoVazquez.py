# Autor: Diego Vázquez
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana una frase i compta quantes vocals conté.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una frase
# Especificacions de sortida
# Imprimeix el nombre de vocals a la frase introduïda
frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOUàèéíòóúÀÈÉÍÒÓÚ"
comptador = 0

for lletra in frase:
    if lletra in vocals:
        comptador += 1

print(f"La frase té {comptador} vocals.")