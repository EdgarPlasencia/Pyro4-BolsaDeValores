import Pyro4

b=Pyro4.Proxy("PYRO:bolsa@localhost:9090")



#b.comprarB(10,1)
#b.venderB(10,1)


def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce una opcion valida')
     
    return num

salir = False
opcion = 0
while not salir:
    print ("===================================================================")
    print("================== Almacenes tu vieja ==============================")
    print ("===================================================================")   
    print ("1.-AGREGAR EMPRESA")
    print ("2.-COMPRAR ACCIONES")
    print ("3.-VENDER ACCIONES")
    print ("4.-LISTA DE EMPRESAS")
    print ("5.-SALIR")
    print ("===================================================================")
    print ("ELIGE UNA OPCION")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        nomE=input("Ingrese el nombre de la empresa:")
        b.agregarE(nomE)
    elif opcion == 2:
        codE=int(input("Ingrese el codigo de la empresa:"))
        numA=int(input("Ingrese el numero de acciones a comprar:"))
        b.comprarB(numA,codE)
    elif opcion == 3:
        codE=int(input("Ingrese el codigo de la empresa:"))
        numA=int(input("Ingrese el numero de acciones a vender:"))
        b.venderB(numA,codE)
    elif opcion == 4:
        b.listar()
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 4")
 
print ("Fin")