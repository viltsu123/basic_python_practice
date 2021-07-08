
def oujee():
    '''Just a thing that print out hello'''
    print("hello")
#lähtee q kirjaimella sit pois helpistä!
#help(oujee)

mystring  = "Koira lähti karkuun ja löysi toisen"
#lyhyt toteaminen funkkarille kun koira in s.lower on jo booleani
def koira(s):
    return "koira" in s.lower()

vaarin = koira("kissa lähti karkuun")
oikein = koira(mystring)

print(oikein)
print(vaarin)


def siansaksa(s):
    '''
    Sianksaksa kääntäjä, toimii parhaiten jenkki sanoilla. Logiikka tulee sieltä puolelta maailmaa.
    OUTPUT: jos alkaa konsonantilla INPUT = koira = oirakay
            jos alkaa vokaalilla INPUT = airo = airoay
    INPUT: antakaa str objekti eli sana
    '''
    firs_letter = s[0]
    if firs_letter in 'aeiouyäö':
        return s + "ay"
    else:
        return s[1:] + firs_letter + "ay"

vastaus = siansaksa("koira")
print(vastaus)

#miten saan usean muuttujan mukaan funkkariin?
def isofunk(*args):
    return sum(args) * 0.01
#*args antaa mahdollisuuden syöttää niin monta argumenttia funkkariin ku haluat.
print(isofunk(3,4,5,6,7,8,9))

#sitten sisään tuleva argumentteja dictionary muodossa, hoidetaan **kwargs argumentilla
def greatfunk(**kwargs):
    if 'omena' in kwargs:
        print("Minusta {} on paras hedelmä".format(kwargs['omena']))
    else:
        print("tervetuloa kauppaan, mitä haluatte?")

greatfunk(omena = 'omenaasdadasd')
#funkkari käsittelee siis argumentteja dictionary muodossa funkkarin sisällä

#args ja kwargs yhessä

def myfucn(*args, **kwargs):
    print(args)
    print(kwargs)
    print("i would like {} {}".format(args[0], kwargs['food']))

myfucn(1,2,3,4, desert = 'jätski', food = 'broileri', animal = 'hamsteri')

def myfunc(*args):
    my_list = []
    for a in args:
        if a %2 == 0:
            my_list.append(a)
    return my_list

lista = myfunc(1,2,3,4)
print(lista)
#thedään funkkari joka palauttaa stringin joka on parillinen kirjain = iso ja pariton = pieni kirjain
print()
def myfunc(s):
    print(s)
    newstring = ""
    counter = 0
    for a in s:
        if counter %2 == 0:
            newstring += s[counter].lower()
            counter += 1
        else:
            newstring += s[counter].capitalize()
            counter += 1
    return newstring

vastaus = myfunc("Heipparallaa")
print(vastaus)

print()
#return true if words begin with same letter, flase if not
testword = "jabadabaduuuu oijdoijsdfoisjdf"
wordlist = testword.split(" ")
print(wordlist[1][0])#should print "o"

def animal_crackers(text):
    words = text.split(" ")
    if words[0][0].lower() == words[1][0].lower():
        return True
    else:
        return False

print(animal_crackers("Lama lama"))

print()

def master_yoda(text):
    words = text.split(" ")
    words.reverse()
    answer = " ".join(words)
    print(answer)
master_yoda("We go home")

print()

def almost_there(n):
    if n < 100:
        if (100 - n) <= 10:
            return True
        else:
            return False
    elif n > 100 and n < 190:
        if (n - 100) <= 10:
            return True
        else:
            return False
    if n < 200:
        if (200 - n) <= 10:
            return True
        else:
            return False
    elif n > 200:
        if (n - 200) <= 10:
            return True
        else:
            return False

vast = almost_there(110)#should return True
vast2 = almost_there(91)#should return True
vast3 = almost_there(89)#False
vast4 = almost_there(111)#fasle
vast5 = almost_there(209)#True
print(vast)
print(vast2)
print(vast3)
print(vast4)
print(vast5)

#if list has two 3 side by side return true, else return false
print()
def has_33(nums):
    counter = 0
    jolly = 0
    list_length = len(nums)
    while counter < list_length - 1:
        #print(counter)
        if nums[counter] == 3 and nums[counter + 1] == 3:
            counter += 1
            jolly += 1
        else:
            counter += 1
    if jolly == 1:
        return True
    else:
        return False

rast = has_33([1,3,3])
rast1 = has_33([3,1,3])
print(rast)#true
print(rast1)#

print()

def blackjack(a,b,c):
    hand = a + b + c
    if hand <= 21:
        return hand
    elif hand > 21:
        hand -= 10
        return hand
    elif hand > 21 and a == 11 or b == 11 or c == 11:
        hand -= 10
        if hand > 21:
            return 'BUST'
        else:
            return hand
kasi = blackjack(9,9,9)
print(kasi)

print()
print("kuusysi ongelma")
ar = [1,2,3,4,6,7,9,10]
#print the sum from a list excluding numbers 6 - 9
#so [1,2,6,9,11] == 14 (1+2+11), ongelma jos on 6 mutta ei 9. silloin ei ota vastaan 10 ->

#eli toimii plussaus tuolla add arvolla. niin kauan kuin add = true niin plussataan arvoja.
#sitten kun tulee 6 vastaan add  = false eli hyppää ulos ekasta whilesta ja menee tokaan.
#sitten tuolla tokassa whilessa, niin kauan kuin ei tuu vastaan 9 niin otetaan seuraava numero.
#sit kun 10 taas tulee niin add = true ja summaus jatkuu ekassa whilessa.
#ongelma tässä on se että jos 9 ei tuu niin 6 jälkee jos on 10 niin sitä ei huomioida.
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    print(total)

summer_69(ar)

#spygame esimerkki, ottaa listan vastaan mitä etsitään,
#sitten jos löytyy listasta vastaus niin etsintä listasta eka pop pois!
#sit kun tsekkaus lista on 1 pituudeltaan palautellaan true!
def spygame(arr):
    code = [0,0,7,'loppu']
    for a in arr:
        if code[0] == a:
            code.pop(0)
    return len(code) == 1 #true

vastaus = spygame([1,2,4,0,0,7,5])
print(vastaus)

#prime määrittäjä....
print()
def primegetter(luku):
    if luku < 2:#tarkistaa että luku ei ole 0,1
        return 0

    primes = [2]#alustetaan lista ekalla priimillä
    counter = 3

    while counter <= luku:
        for y in primes:#vanha tapa= range(3,counter,2); niin kauan kuin y on 3 -- luku alueella, edetään 2 askeleilla.
            if counter%y == 0:#ei ole priimi, tsekkaus. Ekalla kerralla se on 3%2
                counter += 2
                break
        else:
            primes.append(counter)#on priimi, listaan mukaan
            counter += 2
    print(primes)

primegetter(100)
