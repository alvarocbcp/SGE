# EJERCICIO 5

l1 = [2, 5, 6]
l2 = [3, 6, 7]
l3 = [1, 4, 5]

lf = [ele1*ele2*ele3 for ele1, ele2, ele3 in zip(l1, l2, l3)]

print(lf)