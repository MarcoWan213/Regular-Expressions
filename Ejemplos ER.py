#Ejemplos ER

import re

opcion = 0

text = "escrito.txt"

while opcion != 11 :
    
    print("Seleccione una Opcion: "+
    "\n1.Todas las palabras que tengan una longitud de 7 o más letras\n2.Expresiones que NO finalicen con una vocal."
    "\n3.Las palabras que inicien con “M” donde la segunda letra no sea vocal"+
    "\n4.Expresiones encerradas entre comillas"+
    "\n5.Ip’s"+
    "\n6.Horas"+
    "\n7.Telefonos"+
    "\n8.Correos electrónicos"+
    "\n9.Url’s"+
    "\n10.Código postal"+
    "\n11. Salir")

    opcion = int(input ("Digite su eleccion"))

    texto = open(text,"r")

    if opcion == 1:                
        rex = r"[a-zA-Z]+"
        reg = re.compile(rex)        
        for line in texto:
            lista = reg.findall(line)
            rexrex = r"[A-Za-z]{7,}"
            for elemento in lista:
                if re.search(rexrex, elemento):
                    print(elemento)        
    elif opcion == 2:                        
        regex = r"[A-Za-z]+"
        reg = re.compile(regex)
        for line in texto:
            lista = reg.findall(line)
            regex = r"[A-Za-z]+[^aeiou]$"
            for elemento in lista:
                if re.search(regex,elemento):
                    print(elemento)        
    elif opcion == 3:                
        rex = "[M][^aeiouAEIOU]"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elemento in lista:
                if re.search(rex, elemento):
                    print(elemento)        
    elif opcion == 4:                
        rex = r"(\"([^\"]+)\")"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)            
            if re.search(rex, line):
                print(lista)                    
    elif opcion == 5:                
        rex = r"([0-9]{3}\.[0-9]{2}\.[0-9]{1,3}\.[0-9]{1,3})"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elemento in lista:
                if re.search(rex, elemento):
                    print(elemento)        
    elif opcion == 6:                
        rex = r"(\d\d\:\d\d\s[AaPp][Mm])"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)        
    elif opcion == 7:                
        rex = r"(\d\d\d\d\d\d\d\d\d\d)"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)        
    elif opcion == 8:                
        rex = r"([0-9a-zA-Z0-9._%+-]+@[0-9a-zA-Z0-9.-]+\.[0-9a-zA-Z]{2,6})"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)        
    elif opcion == 9:                
        rex = r"(http:|https:\/\/[0-9a-zA-Z0-9._%+-]+\.[0-9a-zA-Z]+\/[^\r\n\s]+)" #TODO @MarcoWan213 Solucionar
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)        
    elif opcion == 10:                
        rex = r"(\d\d\d\d\d)"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)        
    elif opcion == 11:
        print("El programa se ha cerrado")    
    else :
        print("\n opción no valida, vuelva a ingresar una opcion")
    texto.close
    print("\n")
