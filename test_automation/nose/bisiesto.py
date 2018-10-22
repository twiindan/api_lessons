
def es_bisiesto(year):

    if not isinstance(year, int):
        return "Error: Should be a integer"

    if year < 0:
        return "Error: Should be a positive number"

    if year % 100 == 0:
        print "Divisible entre 100"
        if year % 400 == 0:
            return 'Es bisiesto'
        else:
            return 'No es bisiesto'

    elif year % 4 == 0:
        return 'Es bisiesto'
    else:
        return 'No es bisiesto'


