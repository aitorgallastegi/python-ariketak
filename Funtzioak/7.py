x = int(input("Sartu zerrendaren luzeera: "))
zenbakiak = []
def batuketa():
    print(sum(zenbakiak))
for y in range(x):
    zenbakia = int(input("Sartu zenbaki bat: "))
    zenbakiak.append(zenbakia)
batuketa()