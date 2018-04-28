Year = 2018
name = input('What is your name? ')
while True:
    age = input('What is your age? ')
    try:
        age = int(age)
        if age > 100:
            print('Invalid age')
            continue
        break
    except:
        print('Invalid age')
        continue
Year100 = Year + 100 - age
print('You will turn 100 on year', Year100)
