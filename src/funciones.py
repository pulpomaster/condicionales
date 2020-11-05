# -*- coding: utf-8 -*-

def esBisiesto(year):
	return year % 4 == 0

def dayCorrect(day):
	return 1 <= day <= 31

def monthCorrect(month):
	return 1 <= month <= 12

def yearCorrect(year):
	return 1 <= year <= 31

def esFechaValida(date):	
	"""
	 Función para comprobar si una fecha coicide con el formato DD-MM-AA

	 Parameters:
	 date (string): Fecha como string en formato DD-MM-AA

	 Returns
	 boolean: True si la fecha es correcta
	"""
	list = date.split("-")
	day = int(list[0])
	month = int(list[1])
	year = int(list[2])

	if not (dayCorrect(day) and monthCorrect(month) and yearCorrect(year)):
		return False

	if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
		return False

	if month == 2:
		if esBisiesto(year):
			if day > 29:
				return False
		else:
			if day > 28:
				return False
	return True


def erroresDeFecha(date):
	# La fecha ira en el formato 02-10-20
	# Esta funcion tiene dos outputs: El primero sera un booleano y el segundo sera una lista con los errores de la fecha, si los tuviese.
	# En el caso de que la fecha fuese correcta, el segundo output sera un string indicandolo

	list = date.split("-")
	errores = []

	# Intenta convertir los valores de la fecha en string a int. Si fallase, puede devolver directamente un error sin hacer más comprobaciones
	try:
		day = int(list[0])
		month = int(list[1])
		year = int(list[2])
	except ValueError as e:
		errores.append("La fecha no se ha podido convertir a int")
		return False, errores

	if day == 0 or month == 0 or year == 0:
		errores.append('Ninguno de los valores puede ser 0')
		return False, errores

	if not dayCorrect(day):
		errores.append("El día debe estar entre 1-31")
		return False, errores

	if not monthCorrect(month):
		errores.append("El mes debe estar entre 1-12")
		return False, errores

	if month == 2:
		if esBisiesto(year):
			if day > 29:
				errores.append('En años bisiestos febrero no puede tener mas de 29 dias')
		else:
			if day > 28:
				errores.append('Febrero solo tiene 28 dias')
	
	if len(errores) == 0:
		return True, 'La fecha es correcta, ningun error'
	else:
		return False, errores


print(erroresDeFecha("a-2-20"))