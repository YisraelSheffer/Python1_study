while True:
    num = raw_input("Pick a number ")
    try:
        num = int(num)
        break
    except:
        continue
if num % 2 != 0:
    print "ODD! "
else:
    print "EVEN! "
