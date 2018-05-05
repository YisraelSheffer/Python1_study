while True:
    a = input("Pick a number ")
    try:
        a = int(a)
        break
    except:
        print("Invalid ")
for x in range(1,int(a/2)):
    div = a%x
    if (div == 0):
        print (x)
