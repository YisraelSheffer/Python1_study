X = raw_input("Put  a string ")
for i in (0,int(len(X)/2)):
    if X[i] != X[-1-i]:
        print "not polindrom "
        exit()
print "polindrom "
