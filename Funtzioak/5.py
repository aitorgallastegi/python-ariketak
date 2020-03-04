testua = input("Sartu testu bat: ")
hitza = input("Sartu hitz bat: ")
def funtzioa (testua,hitza):
    x = testua.split() # testua listara bihurtzen du
    for y in range(len(x)):
        if x[y]==hitza:
            print(hitza,"testu barruan dago")
funtzioa(testua,hitza)