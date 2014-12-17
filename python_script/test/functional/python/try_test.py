
try:
    with open("x.txt") as f:
       data = f.read()

    raise NameError('HiThere')
except:
    print "Exception"
