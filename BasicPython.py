print(7**4)
print("")
print("break this down to a list of chars: asddfbeergetb")
gibberish = "asddfbeergetb"
theList = [x for x in gibberish]
print("")
print(theList)
print("")
print("Now print this sentence word by word using split")
print("")
words = "Now print this sentence word by word using split"
mylistofwords = words.split(" ")
print(mylistofwords)
print("")
print("Annoying task....")
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
#get hello
print(d.get("k1")[3].get("tricky")[3].get("target")[3])
print("")
print("last speeding chanllenge")
def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed < 66:
            return "No Ticket"
        elif speed > 65 and speed < 86:
            return "Small Ticket"
        elif speed >= 86:
            return "Big Ticket"
    else:
        if speed < 61:
            return "No Ticket"
        elif speed > 60 and speed < 81:
            return "Small Ticket"
        elif speed >= 81:
            return "Big Ticket"
print(caught_speeding(81, True))
print(caught_speeding(81, False))
