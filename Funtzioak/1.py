x = int(input("Sartu zenbaki oso bat: "))
y=1
z=1
def f(x,y,z):
    for y in range (1,x+1):
        z = y*z
        y=y+1
    print(z)
f(x,y,z)