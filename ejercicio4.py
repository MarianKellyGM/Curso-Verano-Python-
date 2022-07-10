#ejercicio 4 - Guzman Mares Marian Kelly 
i=0
historial_suma={"vacio"}
historial_resta={"vacio"}
historial_multiplicacion={"vacio"}
historial_division={"vacio"}
while True:
    entrada=input("¿Desea entrar al sistema?: ")
    if entrada in ("Si","si","SI"):
        print("Menu")
        print("1.Suma\n2.Resta\n3.Multiplicaciòn\n4.Division\n5.Historial")
        eleccion=input("Escriba la operacion que desee realizar: ").lower()
        if eleccion=="suma":
            primer_num=int(input("Ingresa el primer numero de la suma: "))
            segundo_num=int(input("Ingresa el segundo numero de la suma: "))
            suma=primer_num+segundo_num
            print(f"{primer_num}+{segundo_num}={suma}")
            if historial_suma=={"vacio"}:
                historial_suma.remove("vacio")
            historial_suma.add(f"{primer_num}+{segundo_num}={suma}")
        elif eleccion == 'resta':
            primer_num=int(input("Ingresa el primer numero de la resta: "))
            segundo_num=int(input("Ingresa el segundo numero de la resta: "))
            resta=primer_num-segundo_num
            print(f"{primer_num}-{segundo_num}={resta}")
            if historial_resta=={"vacio"}:
                historial_resta.remove("vacio")
            historial_resta.add(f"{primer_num}-{segundo_num}={resta}")
        elif eleccion == 'multiplicacion':
            primer_num=int(input("Ingresa el primer numero de la multiplicacion: "))
            segundo_num=int(input("Ingresa el segundo numero de la multiplicacion: "))
            multi=primer_num*segundo_num
            print(f"{primer_num}x{segundo_num}={multi}")
            if historial_multiplicacion=={"vacio"}:
                historial_multiplicacion.remove("vacio")
            historial_multiplicacion.add(f"{primer_num}x{segundo_num}={multi}")
        elif eleccion == 'division':
            primer_num=int(input("Ingresa el primer numero de la division (denominador): "))
            segundo_num=int(input("Ingresa el segundo numero de la division (dividendo): "))
            division=int(primer_num/segundo_num)
            print(f"{primer_num}/{segundo_num}={division}")
            if historial_division=={"vacio"}:
                historial_division.remove("vacio")
            historial_division.add(f"{primer_num}/{segundo_num}={division}")
        elif eleccion == 'historial':
            if historial_suma == {"vacio"} and historial_resta =={"vacio"} and historial_multiplicacion=={"vacio"} and historial_division=={"vacio"}:
                print("Historial vacio")
            else:
                print("Historial de la suma:",historial_suma)
                print("Historial de la resta: ",historial_resta)
                print("Historial de la multiplicacion: ",historial_multiplicacion)
                print("Historial de la division: ",historial_division)
                eleccion2=input("¿Desea eliminar el historial?: ")
                if eleccion2 in ("Si","SI","si"):
                    historial_suma.clear()
                    historial_resta.clear()
                    historial_multiplicacion.clear()
                    historial_division.clear()
                    historial_suma.add("vacio")
                    historial_resta.add("vacio")
                    historial_multiplicacion.add("vacio")
                    historial_division.add("vacio")
                    print(f"Historial eliminado\nHistorial de la suma:{historial_suma}\nHistorial de la resta:{historial_resta}\nHistorial de la multiplicacion:{historial_multiplicacion}\nHistorial de la division:{historial_division}")
                else:
                    print("No se a eliminado el historial")
        else:
            print("Por el momento no tenemos esta opcion incluida en el menu")
    else:
        break

print("Fuera del sistema")

