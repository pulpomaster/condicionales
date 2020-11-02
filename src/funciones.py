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
		return False, "Error en el numero del dia,mes,"

	if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
		return False

	if month == 2:
		if esBisiesto(year):
			if day >29:
				return False
		else:
			if day>28:
				return False
	return True





def erroresDeFecha(date):
	# La fecha ira en el formato 02-10-20
	# Esta funcion tiene dos outputs: El primero sera un booleano y el segundo sera una lista con los errores de la fecha, si los tuviese.
	# En el caso de que la fecha fuese correcta, el segundo output sera un string indicandolo


	list = date.split("-")
	errores = []

	if len(list) != 3:
		errores.append('Formato incorrecto, el correcto es dia-mes-año')
		return False, errores

	def iint(x):
		if x == '':
			return 6728346589236456283495
		else:
			return int(x)


	day = iint(list[0])
	month = iint(list[1])
	year = iint(list[2])

	if day == 6728346589236456283495 or month == 6728346589236456283495 or year == 6728346589236456283495:
		errores.append('Formato incorrecto, el correcto es dia-mes-año')
		return False, errores

	if day == 0 or month == 0 or year == 0:
		errores.append('Ninguno de los valores puede ser 0')

	if day > 31:
		errores.append('No se puede tener mas de 31 dias')

	if month > 12:
		errores.append('No se puede tener mas de 12 meses')


	if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:		# meses con 30 dias
		errores.append('Ese mes no puede tener mas de 30 dias')

	if month == 2:
		if esBisiesto(year):
			if day >29:
				errores.append('En años bisiestos febrero no puede tener mas de 29 dias')
		else:
			if day>28:
				errores.append('Febrero solo tiene 28 dias')
	
	if len(errores) == 0:
		return True, 'La fecha es correcta, ningun error'
	else:
		return False, errores

