print('hello world')

a = 4
j = "Hello"
#gets the first letter produces = H
print(j[0])
#from the start upto but not including 3rd char produces = Hel
print(j[:3])
print(j)
#get a specific part produces = lo
print(j[3:5])
#jump in steps produces = Hlo
print(j[::2])
#revrse the string
print(j[::-1])
#get last letter from string
print(j[-3])

#strings are immutable:
name  = "Sam"
print(name)
#this can not be changed anymore
#to change the name to Pam we can do string concatination
last_letters = name[1:]
modifiedName = "P" + last_letters
print(modifiedName)
#some methods in the stirng object:
print(modifiedName.upper())
#this does not change the original stinrg
print(modifiedName)
#split() is very fun, default separates by whitespace: result is a list
print(modifiedName.split())
#split can take a character to split the line by: this will override the whitespace removal, will include whitespace
print(modifiedName.split('a'))

#inserting strings to a string:
print("{} is a very nice person".format(modifiedName))
print("I went on a picnic with {} and we had a {} time".format(modifiedName, "lovely"))
#works with indexing also, first jumbled:
print("What {} {} {}".format("day", "a", "lovely"))
#and then the right way around:
print("What {1} {2} {0}".format("day", "a", "lovely"))
#will work with the variable assignment method:
print("What {a} {l} {d}".format(d="day", a="a", l="lovely"))

#printing float values with precision:
result = 1/18
#lets get 5 numbers after the point: r is the number, 1 is the spacing, 5 is the amount of numbers after the point and f is for flair
print("The result was {r:1.5f}".format(r=result))
#another way to do this:
name="Sammy"
age=45
print(f'{name} is {age} years old')

#lists
print("Lists coming up")
print("")
mylist = [1,2,3,4,"heloou", "yjjejejej", 1.5]
print(mylist)
#indexing
print(mylist[3])
#slicing
print(mylist[3:6])
#concatination
anotherList = [2,5,6,"another list"]
newList = mylist + anotherList
print(newList)
#just like string but now we can chnage the values
newList[0] = "I just changed the first object to this sentence."
print(newList)
#adding items to end of list
newList.append("Last item added")
print(newList)
#removing last items; the pop() removes the last item in list and returns it
removedItem = newList.pop()
print(removedItem)
print(newList)
#does work based on index location as well
print()
print("Removing an item based on index from a list:")
newList.pop(0)
print(newList)
print()
print("Sorting a list")
#newList.sort()
#print(newList) will throw an error, can not sort str and int mixed lists
wordlist = ['a','b','r','f','i','d']
print(wordlist)
wordlist.sort()
print(wordlist)
numberlist = [3,1,2,5,6,3,4,5,6,9,87,6]
print(numberlist)
numberlist.sort()
print(numberlist)
#reverse a list
print()
print("Reverse a list")
print(numberlist)
numberlist.reverse()
print(numberlist)
#reverse and sort do not return a new list, happens in place
