""" 
print("Forma 1 de usar modulos de paquetes, esta es: \n")
from matematicas import suma 
from matematicas import resta
from matematicas import multiplicacion
from matematicas import division

print("Suma dos numeros: ")
suma.suma_dos(1, 2)
print("Suma tres numeros: ")
suma.suma_tres(3, 4, 5)

print("resta dos numeros: ")
resta.resta_dos(1, 2)
print("resta tres numeros: ")
resta.resta_tres(3, 4, 5)

print("division dos numeros: ")
division.dividir_dos(1, 2)

print("multiplicacion dos numeros: ")
multiplicacion.multiplicar_dos(1, 2)
print("multiplicacion tres numeros: ")
multiplicacion.multiplicar_tres(3, 4, 5)
"""
"""
print("Forma 2 de usar modulos de paquetes, esta es: \n")

from matematicas.suma import suma_dos
from matematicas.resta import resta_tres
from matematicas.division import dividir_dos
from matematicas.multiplicacion import multiplicar_tres

suma_dos(2, 5)
resta_tres( 4, 2, 1)
dividir_dos(100, 5)
multiplicar_tres(1.3, 9, 5)
"""



print("Forma 3 de usar modulos de paquetes, esta es: \n")

from matematicas.suma import suma_dos as sm_d
from matematicas.resta import resta_tres as rt_t
from matematicas.division import dividir_dos as dv_d
from matematicas.multiplicacion import multiplicar_tres as mp_t

sm_d(2, 5)
rt_t( 4, 2, 1)
dv_d(100, 5)
mp_t(1.3, 9, 5)


"""
print("Forma 4 (No recomendada por posibles casualidades de conflictos), esta es: \n")

from matematicas.suma import * 
from matematicas.resta import * 
from matematicas.division import *
from matematicas.multiplicacion import *

suma_dos(2, 15)
suma_tres(1, 3, 6)

resta_tres( 4, 2, 1)
resta_dos(10, 2)

dividir_dos(180, 6)

multiplicar_tres(3, 9, 5)
multiplicar_dos(5, 5)
"""