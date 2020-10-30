# -*- coding: utf-8 -*-

def esBisiesto(ano):
	if ano%4==0:
		return True
	else:
		return False

#print(esBisiesto(2020))


def esFechaCorrecta(date):	# la fecha ira en el formato 02-10-20
	list = date.split("-")
	day = int(list[0])
	month = int(list[1])
	year = int(list[2])

	if day > 31 or month > 12 or day < 0 or month <0 or year <0:
		return False

	if month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
		return False

	if month == 2:
		if esBisiesto(year):
			if day >29:
				return False
		else:
			if day>28:
				return False
	return True

print(esFechaCorrecta("29-2-21"))