from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from show import mostrar_ingredientes
from tiempo import estimar_tiempo
import datos as d 
import time
import os
import sys
clear='cls' if sys.platform =='win32' else 'clear'

ingredientes_orden = d.ingredientes
print("Gracias por Ordenar con Nosotros")
while True:
 os.system(clear)
 opcion = opcion = input(d.menu)
 
 if opcion == '1':
    os.system(clear)
    eleccion = input(d.T_MASA).upper()
    ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)
    time.sleep(3)
 elif opcion == '2':
    os.system(clear)
    eleccion = input(d.T_SALSA).upper()
    ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)
    time.sleep(3)
    
 elif opcion == '3':
    os.system(clear)
    eleccion = int(input(d.AG_INGREDIENTE))
    ingredientes_orden = agregar_ingrediente(ingredientes_orden,eleccion)
    time.sleep(3)
 elif opcion == '4':
  os.system(clear)
  eleccion = int(input(d.QT_INGREDIENTE))
  ingredientes_orden = quitar_ingrediente(ingredientes_orden,eleccion)
  time.sleep(3)
 
 elif opcion == '5':
    os.system(clear)
    tiempo = estimar_tiempo(ingredientes_orden)
    print(f'Su Pizza estará lista en {tiempo} minutos')
    ordenar = input('Desea ordenar ahora S/N: ').upper()
    if ordenar == 'S':
            print('Gracias por ordenar en Pizza JAT')
            print('Disfrute su Pizza')
            exit()
    time.sleep(3)
 elif opcion == '0':
    os.system(clear)
    mostrar_ingredientes(ingredientes_orden)
    time.sleep(3)
    
 else:
    os.system(clear)
    print('Su pedido ha sido cancelado. Gracias por contactarse a Pizza JAT')
    time.sleep(3)
    exit()
    
    
    

