zenbakiak = []
x = 1
def batazBestekoa(zenbakiak,x):
    while not (x==0):
        x = int(input("Sartu zenbaki bat (0 bukatzeko): "))
        zenbakiak.append(x)
    zenbakiak.pop(-1)
    print("Sartutako zenbakien bataz bestekoa",sum(zenbakiak)/len(zenbakiak),"da")
batazBestekoa(zenbakiak,x)