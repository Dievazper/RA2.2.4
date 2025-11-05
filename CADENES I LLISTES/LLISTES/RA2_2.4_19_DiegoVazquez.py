# Autor: Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari una llista de números i multiplica tots els elements per 2.

# Especificacions d'entrada

# Especificacions de sortida
numeros = []
quantitat = int(input("Quants números vols introduir? "))

for i in range(quantitat):
    num = float(input(f"Introdueix el número {i + 1}: "))
    numeros.append(num)
multiplicats = [num * 2 for num in numeros]

print(f"Llista original: {numeros}")
print(f"Llista multiplicada per 2: {multiplicats}")