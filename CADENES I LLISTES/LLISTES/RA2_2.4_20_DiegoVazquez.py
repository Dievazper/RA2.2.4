# Autor: Diego Vázquez
# Data: 5-11-25

#Descripció del programa o enunciat de l'exercici:
#Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi una llista de paraules separades per espais
# Especificacions de sortida
# Imprimeix la llista de paraules que comencen per vocal
vocals = "aeiou"
paraules_usuari = []
num_paraules = int(input("Quantes paraules vols introduir? "))

for _ in range(num_paraules):
    paraules_usuari.append(input("Introdueix una paraula: "))
paraules_vocals = [p for p in paraules_usuari if p[0].lower() in vocals]

print(f"\nLlista completa: {paraules_usuari}")
print(f"Paraules que comencen per vocal: {paraules_vocals}")