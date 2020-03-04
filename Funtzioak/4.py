zenbakiak1 = []
zenbakiak2 = []
def karratua(zenbakiak1,zenbakiak2):
    x = 1
    while not (x==0):
        x = int(input("Sartu zenbaki bat (0 bukatzeko): "))
        zenbakiak1.append(x)
    zenbakiak1.pop(-1)
    for y in range(len(zenbakiak1)):
        z = (zenbakiak1[y]*zenbakiak1[y])
        zenbakiak2.append(z)
    print(zenbakiak2)
karratua(zenbakiak1,zenbakiak2)