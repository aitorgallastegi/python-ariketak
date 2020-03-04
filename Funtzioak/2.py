import math
erradioa = int(input("Sartu zirkuluaren erradioa: "))
def azalera(erradioa):
    return(math.pi*erradioa*erradioa)
def bolumena(erradioa):
    return ((4/3)*(azalera(erradioa)*erradioa))
print(azalera(erradioa))
print(bolumena(erradioa))