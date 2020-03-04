zenbakiak = []
def maximoa(zenbakiak):
    x = 1
    while not (x==0):
        x = int(input("Sartu zenbaki bat (0 bukatzeko): "))
        zenbakiak.append(x)
    zenbakiak.pop(-1)
    print("Zenbaki handiena",max(zenbakiak),"da")
maximoa(zenbakiak)
