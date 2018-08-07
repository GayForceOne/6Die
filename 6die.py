x = int(raw_input("Dice Size: "))
y = int(raw_input("Roll Count: "))
print "Results"
for number in range(y):
    from random import *
    print randint(1, x)