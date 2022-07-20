#Reloj
import os
import time

entrada = input("Ingrese la hora hora:minutos:segundos de esta manera: ")
lista = entrada.split(":") ## 5:12:41 - ["5", "12", "41"]
print(lista)
if len(lista)==1:
    print("El formato que ingreso no es correcto, recuerde ingresar la hora de la siguiente manera:\n12:24:45")
# if entrada.split("/","-",""):
#     print("El formato que ingreso no es correcto, recuerde ingresar la hora de la sieuinte manera:\n12:24:45")
else:
    e_hora = int(lista [0])
    e_minuto = int(lista[1])
    e_segundo = int(lista[2])
    if e_hora>=1 and e_hora<=24 and e_minuto>=1 and e_minuto<=60 and e_segundo>=1 and e_segundo<=60:
        for hora in range(e_hora, 24):
            for minuto in range(e_minuto, 60):
                for segundo in range(e_segundo, 60):
                    os.system("cls")
                    print(f"{hora}:{minuto}:{segundo}")
                    time.sleep(1)
            
                    if segundo == 59:
                        segundo = 0
                        e_segundo = 0
        
                if minuto == 59:
                    minuto = 0
                    e_minuto = 0 
        
            if hora == 23:
                hora = 0
                e_hora = 0
    else:
        print("La hora que desea ingresar es incorrecta, ingrese una hora real")
