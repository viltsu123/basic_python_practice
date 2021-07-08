theValue = "oshaosghafguadfibadfibadfbaibogdijsfogb"

mylis = []

for x in theValue:
    mylis.append(x)

print("List creation the old way:")
print(mylis)
print()
print("List Comprehension used:")
print()

mylist = [x for x in theValue]
print(mylist)

print()
print("Now some arithmetic operations inside the comprehension")
print()
numbers = [num for num in range(0,11)]
num_operations = [((9/5)*x + 32) for x in numbers if x%2]
print("A list from 1-10, every number is operated on and then added to new list if they are even:")
print()
print(num_operations)
print()
print("and now the list that has everything, evens and odds")
print()
num_operations = [((9/5)*x + 32) for x in numbers]
print(num_operations)
print()
print("Tuples unpacking")
print()
tupleslist = [(1,2),(3,4),(5,6),(7,8)]
for a,b in tupleslist:
    print(a)
    print(b)
print()
print("Test testing :)")
st = 'Print every word in this sentence that has an even number of letters'
words = st.split(" ")
for x in words:
    if(len(x) %2 == 0):
        print(x)
