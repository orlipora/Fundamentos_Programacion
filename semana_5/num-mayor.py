import random

lis_1 = []

for i in range(10):
    lis_1 .append(random.randint(0,100))
    mayor = lis_1[0]
    for i in range(len (lis_1)):
    
        if lis_1[i] >= mayor :
             mayor = lis_1[i]

print(lis_1)
print( "el mayor es : ", mayor )



