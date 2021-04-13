
#x = lambda x: x + lambda x: 5 + x
f = lambda a = 2, b = 3:lambda c: a+b+c



print((lambda x=5, y=5: y+x+(lambda x=2:x+2)())())
