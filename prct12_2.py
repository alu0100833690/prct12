#!/usr/bin/python
#! encoding: UTF-8

import time
import timeit
import modulo

start=time.time()
lista=[]

def error(intervalos,test,umbral):
  fallos=0
  for i in range (test):
    s=modulo.f(intervalos)
    error=abs(s-modulo.PI)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/test)*100)

if __name__=="__main__":
   import sys
   
   if((len(sys.argv) == 1) or (len(sys.argv) == 4)):
     print("No ha introducido todos los argumentos")
     n=200
     v=12
     p=0.2
     
   else:
     n=int(sys.argv[1])
     v=int(sys.argv[2])
     p=float(sys.argv[3])
   s=error(n,v,p)
   print "El porcentaje de error es: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tardó el proceso es de: %14.13f" %finish
   lista=lista+[finish]
   print "Proporcione un nombre para el fichero donde se guardarán los resultados:"
   nombre_fichero= raw_input();
   f=open(nombre_fichero, 'w')
   f.write('El tiempo final es:')
   f.write(str(lista[0]) + '\n')
   f.close()