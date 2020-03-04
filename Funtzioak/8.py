zenbakiak = []
x = 1
def biderketa(zenbakiak):
    z=1
    for y in range(0,len(zenbakiak)):
        z=z*zenbakiak[y]
    print(z)
while not (x==0):
    x = int(input("Sartu zenbaki bat (0 bukatzeko): "))
    zenbakiak.append(x)
zenbakiak.pop(-1)
biderketa(zenbakiak)