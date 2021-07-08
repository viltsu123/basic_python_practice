'''
id number generator.
Should generate a valid finnish hetu number.
'''
from calendar import monthrange
from random import randint

CHECK_KEYS = "0123456789ABCDEFHJKLMNPRSTUVWXY"
CENTURIES = {'18':'+','19':'-','20':'A'}

def generator():
	year = randint(1940, 2001)
	month = randint(1, 12)
	day = randint(1, monthrange(year, month)[1])

	century_sep = CENTURIES[str(year)[0:2]]

	order_num = randint(2, 889)

	check_number = "%02d%02d%s%03d" % (day, month, str(year)[0:2],
									   order_num)

	check_number_index = int(check_number)%31
	key = CHECK_KEYS[check_number_index]

	return "%02d%02d%s%s%03d%s" % (day, month, str(year)[0:2],
							 century_sep, order_num, key)
