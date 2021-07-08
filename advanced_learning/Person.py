'''
The Person class. This is the object class for Person.
'''
import IdNumber
from random import randint

#names to use, selected randomly

class Person:
    def __init__(self):
        #generate id
        idn = IdNumber.generator()
        firstn = ""

        malenames = ['Jussi', 'Kari', 'Teppo', 'Teemu', 'Lauri', 'Rami', 'Jaakko']
        femalenames = ['Tuija', 'Riikka', 'Saija', 'Satu', 'Reetta', 'Kiira', 'Paula']
        lastnames = ['Sallinen', 'Huokunen', 'Tapola', 'Juntunen', 'Kukkola', 'Heikkilä', 'Laurila', 'Rehnsted']

        #define gender
        if int(idn[7:10]) % 2:
            firstn = malenames[randint(0,6)]
        else:
            firstn = femalenames[randint(0,6)]

        self.id = idn
        self.firstname = firstn
        self.lastname = lastnames[randint(0,7)]

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.id
