# Tarea_1
# Steven Arias Madrigal
# Luis Pablo Sibaja Perez
##############################################################################
class Tarea1:
    # Se define la funcion "string_work"
    def string_work(string):
        # Se revisa que el parametro de entrada sea de tipo string
        if isinstance(string, str):
            # Se revisa que el string de entrada contenga unicamente caracteres
            # de la A la Z
            if string.isalpha():
                # Realiza el cambio de mayusculas por minusculas y viceversa
                return string.swapcase()
            else:
                # Codigo de error al ingresar un string con numeros o simbolos
                return -100
        else:
            # Codigo de error al no ingresar un string
            return -101
    ###########################################################################

    ###########################################################################
    # Se define la funcion "num_to_str"
    def num_to_str(numero):
        # Se crean tuplas que haran de base de datos para la funcion
        unidades = ("cero", "uno", "dos", "tres", "cuatro", "cinco",
                    "seis", "siete", "ocho", "nueve")
        diez = ("diez", "once", "doce", "trece", "catorce", "quince",
                "dieciseis", "diecisiete", "dieciocho", "diecinueve")
        veinte = ("veinte", "veintiuno", "veintidos", "veintitres",
                  "veinticuatro", "veinticinco", "veintiseis", "veintisiete",
                  "veintiocho", "veintinueve")
        decenas = ("cero", "diez", "veinte", "treinta", "cuarenta",
                   "cincuenta", "sesenta", "setenta", "ochenta", "noventa")
        # Se verifica que la entrada sea un numero
        if isinstance(numero, int):
            # Se reivisa que el numero cumpla con los parametros
            if numero >= 0 and numero <= 99:
                # Se divide el numero en unidades y decenas
                u = numero % 10
                d = numero // 10
                # Se escribe en texto en la variable resultado
                if d > 2:
                    resultado = decenas[d]
                    if u != 0:
                        resultado = resultado + "_y_" + unidades[u]
                if d == 2:
                    if u == 0:
                        resultado = decenas[d]
                    else:
                        resultado = veinte[u]
                if d == 1:
                    resultado = diez[u]
                if d == 0:
                    resultado = unidades[u]
                # Se retorna el resultado
                return resultado
            else:
                # Se retorna el valor de Error Value Parameter
                return -53
        else:
            # Se retorna el valor de Error Value Number
            return -50
    ###########################################################################
