# Tarea 1
# Steven Arias Madrigal
# Luis Pablo Sibaja Perez
##############################################################################
from Metodos import Tarea1


# Prueba que verifica todos los numeros del 0 al 99
def test_num_to_str_1():
    numero = 0
    while numero != 100:
        assert isinstance(Tarea1.num_to_str(numero), str)
        numero += 1


# Prueba para comprobar que el error al no recibir un numero es el numero -50
def test_num_to_str_2():
    assert Tarea1.num_to_str("numero") == -50


# Prueba para comprobar que el error al no recibir un numero fuera de los
# parametros es el numero -53
def test_num_to_str_3():
    numero = -10
    assert Tarea1.num_to_str(numero) == -53
    numero = 10.5
    # Se retorna el valor -50 ya que se e introduce un flotante
    assert Tarea1.num_to_str(numero) == -50
    numero = 100
    assert Tarea1.num_to_str(numero) == -53


# Verifica que la funcion pueda cambiar de mayusculas a minusculas y
# viceversa todos los caracteres del alfabeto de la A a la Z
def test_string_work_1():
    string = "ABCdefGHIjklMNÑopqRSTuvwXYZ"
    assert Tarea1.string_work(string) == "abcDEFghiJKLmnñOPQrstUVWxyz"
    string = "abcDEFghiJKLmnñOPQrstUVWxyz"
    assert Tarea1.string_work(string) == "ABCdefGHIjklMNÑopqRSTuvwXYZ"


# Verifica que la funcion reconozca un numero y returne el codigo de error
def test_string_work_2():
    string = 21
    assert Tarea1.string_work(string) == -101


# Verifica que la funcion reconozca sibolos y numeros en un string
# y returne el codigo de error unico
def test_verify_3():
    string = "Luis_Pabl0"
    assert Tarea1.string_work(string) == -100
