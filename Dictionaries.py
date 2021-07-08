my_dictionary = {'key1': 'vp'}
print(my_dictionary['key1'])
pricelist = {'apple': 2.45, 'banana':3.21, 'pears':1.2}
print(f"Price check on bananas, price is {pricelist['banana']}")
#or the .format method
print("Price check on bananas, price is {}".format(pricelist['banana']))

#and ofcourse dictionaries and lists inside dictionaries
myscrambledllist = {'first': 123, 'second':{'insider':'im a dictionary inside a dictionary'}, 'evenWeirder':['oju', 123, {'dictionary': {'nested': 'dictionary insisde a dictionary inside a list'}}]}
print(myscrambledllist['evenWeirder'][2]['dictionary']['nested'])

#adding removing overwriting to my_dictionary
my_dictionary['key2'] = 'joona'
print(my_dictionary)

#overwriting
my_dictionary['key2'] = 'JoonakoMuokattu'
print(my_dictionary)

#Removing
popedItem = my_dictionary.pop('key2')
print(popedItem)
print(my_dictionary)

#Keys inside the dictionary, key
print(my_dictionary.keys())
#items in the dictionary, key:value
print(my_dictionary.items())
#values int he diciotnary, value
print(my_dictionary.values())
