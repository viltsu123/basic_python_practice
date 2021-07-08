#holds unique objects, if you have 'a' in the set there can not be another 'a'
myset = set()
myset.add(9)
myset.add(3)
#unordered collection of any items you want
print(myset)
#try to add 9
myset.add(9)
print(myset)
#did not throw and erro but printed {9, 3} so no adding occurred

#a very useful aspect of set:
mylist = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
#to get distinct values from mylist
newset = set(mylist)
print(newset)
#Sets do not have order! unordered!
