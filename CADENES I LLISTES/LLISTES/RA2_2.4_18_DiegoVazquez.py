# Autor: Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari una llista d'elements
#Escriu una funció que retorni la llista al revés (sense reverse()).

# Especificacions d'entrada
# Especificacions de sortida
llista = []

quantitat = int(input("Quants elements vols introduir a la llista? "))

for i in range(quantitat):
    element = input(f"Element {i + 1}: ")
    llista.append(element)

llista_girada = llista[::-1]

print(f"Llista original: {llista}")
print(f"Llista girada: {llista_girada}")