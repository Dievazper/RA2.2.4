# Autor: Diego Vázquez
# Data: 31-10-25

#Descripció del programa o enunciat de l'exercici:
#Crea una llista amb 5 nombres i imprimeix el major i el menor.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi 5 nombres
# Especificacions de sortida
# Imprimeix el nombre major i el nombre menor de la llista
nombres = []
print("Introdueix 5 números, un per un:")

for i in range(5):
    num = int(input(f"Número {i+1}: "))
    nombres.append(num)

major = max(nombres)
menor = min(nombres)

print(f"La llista que has introduït és: {nombres}")
print(f"El número més gran és: {major}")
print(f"El número més petit és: {menor}")

