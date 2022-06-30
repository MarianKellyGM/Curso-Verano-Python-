#Ejercicio 1

print("\nIngrese los siguientes datos")
nombre=input("Ingresa tu nombre: ")
numtelefono=int (input("Ingresa tu numero de telefono: "))#declaras el tipo de dato por que python ingresa puras cadenas las conviertes al tipo de dato que quieres que sea
direccion=input("Ingresa tu direccion: ")
edad=int(input("Ingresa tu edad: "))
Nacionalidad=input("Ingresa tu nacionalidad: ")
FechaNacimiento=input("Ingresa tu fecha de nacimiento: ")
altura=float(input("Ingresa tu altura: "))
peso=float(input("Ingresa tu peso: "))
print("Datos\n", nombre,"\n",numtelefono,"\n",direccion,"\n",edad,"\n",Nacionalidad,"\n",FechaNacimiento,"\n",altura,"\n",peso)
print("Tipo de Dato\n",type(nombre),"\n",type(numtelefono),"\n",type(direccion),"\n",type(edad),"\n",type(Nacionalidad),"\n",type(FechaNacimiento),"\n",type(altura),"\n",type(peso))
#type es para ver el tipo de dato que esta guardando esa variable 