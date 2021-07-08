#does nothing but will throw error if file not in same directory as running script
myfile = open('test.rtf')
#mywrongfile = open('whoops.rtf')

#reads the whole info, metadata, text
print(myfile.read())
print()
print('Trying to read again')
print(myfile.read())
#did not read anything because cursor is at the end of txt file
#bring cursor back to beginning
myfile.seek(0)
#then read again
print('File cursor returned to 0, beginnign to read:')
print()
print(myfile.read())
myfile.seek(0)
print()
print()
print()
print()
#get lines of text as a list
print(myfile.readlines())
#opening the file on your desktop for example
print()
print()
print()
print()
print('Reading from the desktop')
print()
mynewfile = open('/Users/Sweethomealabama/Desktop/thistest.rtf')
print(mynewfile.readlines())
myfile.close()
mynewfile.close()
print()
print()
print('Using the with as to open close file')
print()

#using tyylinen lause, tekee käsittelyn ja sulkee tiedoston heti kun blokki ohi
with open('test.rtf') as myotherfile:
    content = myotherfile.read()

print(content)
print()
print()
print('Lisäämistä fileeseen')
print()

#sit mode='r' readille, mode='w' yli kirjoittamiselle ja mode = 'a' tekstiin lisäämiselle
with open('test.rtf', mode='a') as myappendablefile:
    addendum = ' tämä on ihanaaa'
    myappendablefile.write(addendum)

with open('test.rtf', mode='r') as f:
    contents = f.read()

print(contents)
