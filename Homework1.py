#volume of sphere = (4/3)*pi*r**3
import math

def rad(r):
    return (4/3)*math.pi*r**3

print(rad(2))
print()
#check if number between numbers in list
def ran_check(num,low,high):
    checklist = range(low,high)
    if num in checklist:
        return "The number was there, bitch"
    else:
        return "No number between those higs and lows"
#the same but with bool return
def ran_bool(num,low,high):
    checklist = range(low,high)
    if num in checklist:
        return True
    else:
        return False

print(ran_check(5,2,7))
print(ran_check(9,3,8))
print(ran_bool(3,1,10))
print(ran_bool(13,1,100))
print(ran_bool(13,1,10))
print()
name = "asdasdasd"

#count uppercase letter from string and lower case letters
def up_low(s):
    low = 0
    high = 0
    words = s.split(" ")
    for a in words:
        counter = len(a)
        i = 0
        while i < counter:
            if a[i].isupper():
                high += 1
                i += 1
            elif a[i].islower():
                low += 1
                i += 1
            else:
                i += 1
    print(f'Found {high} uppercase letters!')
    print(f'Found {low} lowercase letters')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
#print out unique numbers in a list [1,1,1,1,,2,2,2,2,,3,3,3,3,] = [1,2,3]
def unique_list(lst):
    answerlist = []
    thething = set(lst)
    for a in thething:
        answerlist.append(a)
    return answerlist

answer = unique_list([1,1,1,2,2,3,3,3,3])
print(answer)
print()
#multiply all the numbers in a list
def multiply(numbers):
    max = 1
    for a in numbers:
        max *= a
    print(max)

multiply([1,2,3,4])#expected 24
print()
#palindromi tarkistaja
def palindrome(s):
    s = s.replace(' ', '')
    print(s)
    return s == s[::-1]#jos tosi niin True returnaa, muutoin False

print(palindrome('saippuakauppias'))
print()

import string

def ispangram(str1, alphabet=string.ascii_uppercase):
    str1 = str1.upper()
    str1 = str1.replace(' ','')
    lisu = []
    vastaus = ""
    saia = set(str1)
    for a in saia:
        lisu.append(a)
    lisu.sort()
    for s in lisu:
        vastaus += s
    if vastaus == alphabet:
        return True
    else:
        return False

def kirjavastaus_ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram('The quick brown fox jumps over the lazy dog'))
