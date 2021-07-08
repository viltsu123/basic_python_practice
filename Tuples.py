#these are immutable, no changing!
t = (1,2,3,4,5,6,7,8,1)
print(type(t))

#works like a list
print(t)
#indexing
print(t[1])
#get last one
print(t[-1])
#start from index 1 go to 9 with steps of 2
print(t[1:9:2])
#count specific objects
howManyOnes = t.count(1)
print(howManyOnes)
