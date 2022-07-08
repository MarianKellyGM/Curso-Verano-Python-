#Ejercicio3-Guzman Mares Marian Kelly

verduras={"brocoli":8.55,"pepino":6.87,"calabaza":11.55,"chayote":14.33}

while True:
    opcion=input("¿Desea comprar un producto de nuestro almacen?\nSi\nNo\n")
    
    if opcion in ("No","no","NO"):
        break
    else:
        entrada=input("Ingresa la verdura que quieres comprar: ").lower()
        if entrada in verduras:
            kilos=int(input("¿Cuantos kilos comprara? "))
            total=round(verduras[entrada]*kilos,2)
            print(f"\nProducto: {entrada}\nPrecio: ${verduras[entrada]}\nKilos comprados: {kilos}\nTotal: ${total}\n")
        else:
            print("\nEse producto no se encuentra en venta")
print("\nGracias por su visita :)")