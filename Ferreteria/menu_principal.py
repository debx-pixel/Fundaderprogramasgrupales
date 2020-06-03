
import sys
productos = [["0","Taladro  ",39.99],
                          ["1","Sierra caladora",25.99],
                          ["2","Esmeril",30.99],
                          ["3","Cinta métrica", 5.99],
                          ["4","Pistola de calor",49.99],
                          ["5","Segueta",5.99],
                          ["6","Gafas de seguridad",2.99],
                          ["7","Guantes",4.99],
                          ["8","Caja de herramienta",25.99],
                          ["9","Juego de brocas",11.95],
                          ["10","Máscara de soldar",34.95],
                          ["11","Escuadra",5.90],
                          ["12","Serrucho",7.80],
                          ["13","Pulidora",54.95],
                          ["14","Cautin",20.95],
                          ["15","Prensa",3.40],
                          ["16","Sierra",199.99],
                          ["17","Maso",25.85],
                          ["18","Alicate",7.50],
                          ["19","Martillo",6.25]
                          ]
                        
print("----------------------------------")
print("    Ferretería el Gran Almacen    ")
print("----------------------------------")
print("1. Realizar compra")
print("2. Realizar cotización")
print("3. Salir")
opc = int(input("respuesta ---> "))
if opc == 1:
    print("Metodo de compras")
    #Metodo de compras
elif opc == 2:
    print("Metodo de cotización")
    #Metodo de cotizacion
elif opc == 3:
    print("Que tenga un buen día!!!")
    print("Vuelva pronto")
    sys.exit(0)
else:
    print("Por favor teclee un valor válido")
    #Vuelve al menu
