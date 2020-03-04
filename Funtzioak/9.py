testua = input("Sartu testu bat: ")
maiuskula = 0
minuskula = 0
def letrak(maiuskula,minuskula):
    for x in testua:
        if x == x.upper():
            maiuskula +=1
        elif x == x.lower(): # espazio hutsek minuskula bezela kontatzen dute
            minuskula +=1
    print(minuskula,maiuskula)
letrak(maiuskula,minuskula)