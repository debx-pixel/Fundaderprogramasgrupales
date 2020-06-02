from os import system, name
import random
import time
import sys
from Pasarela import PaymentGateway
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

pasarela_tarjeta = PaymentGateway()
#Apore de josé modificado
class calculos:
    def __init__(self):
        self.total_compra = 0
        self.desc = 0
        self.desc_porc = ""

    def calcular_compras(self,subto,pregunta_cot):
        subtotal1 = 0
        calc_itbms = 0
        subtotal1 = subto
        calc_itbms = subtotal1 * 0.07
        total = subtotal1 + calc_itbms
        if pregunta_cot == 's' or pregunta_cot == 'S':
            if total >= 100.00 and total < 200.00:
                self.desc = total * 0.10
                self.desc_porc = "10%"
            elif total >= 200.00 and total < 600.00:
                self.desc = total * 0.15
                self.desc_porc = "15%"
            self.total_compra = total - self.desc
        else:
            self.desc_porc = "No hay"
            self.desc = 0
            self.total_compra = total
        print("---------------Cuenta---------------")
        print("")
        print("Total a pagar: ",round(self.total_compra,2),"\n")
        print("------------------------------------\n\n")
calc = calculos()

#Aporte de Nayib modificado
class metodo_pagos:
    def __init__(self):
        self.diferencia = 0
        self.monto = 0

    def pago(self):
        print("Teclee el monto a pagar: ")
        self.monto = float(input("---> "))
        cuenta = calc.total_compra
        if self.monto > cuenta:
            self.diferencia = self.monto - cuenta
        else:
            print("Dinero insuficiente...")
            print("Volviendo...")
            self.pago()
    
    def tarjeta(self):
        pasarela_tarjeta.transaccion()
        pasarela_tarjeta.tarjeta_ingreso()
        print("Teclee el monto a pagar: ")
        self.monto = float(input("---> "))
        cuenta = calc.total_compra
        if self.monto > cuenta:
            self.diferencia = self.monto - cuenta
        else:
            print("Dinero insuficiente...")
            print("Volviendo...")
            self.tarjeta()
    
    def enlinea(self):
        cuenta = calc.total_compra
        if cuenta > 1000.00:
            print("Error de transacción, la compra sobre pasa los 1000.00 dólares")
            print("Regresando... ")
            self.menu_pago()
        else:
            self.tarjeta()

    def menu_pago(self):
        print("\n\nMétodo de pago")
        print("1. Efectivo")
        print("2. Cheques")
        print("3. Tarjeta")
        print("4. En línea")
        pago_opc = int(input("respuesta---->  "))
        if pago_opc == 1:
            self.aux = 10
            self.pago()
        elif pago_opc == 2:
            self.aux = 11
            self.pago()
        elif pago_opc == 3:
            self.aux = 12
            self.tarjeta()
        elif pago_opc == 4:
            self.aux = 13
            self.enlinea()
        else:
            print("Por favor teclee un valor válido")
            time.sleep(2)
            clear()
            self.menu()

met_pagos = metodo_pagos()

class tipo_trans:
    def tipo_transaccion(self,verif):
        if verif == 10:
            trans = "EFECTIVO"
        elif verif == 11:
            trans = "CHEQUE"
        elif verif == 12:
            trans = "TARJETA"
        elif verif == 13:
            trans = "EN LINEA"
        return trans

tipo_pago = tipo_trans()

class llamada_principal:
    def __init__(self):
        self.subt = 0
        self.resp = 's'
        self.doc_aux = 0
        self.titulo = "EL GRAN ALMACEN"
        self.tel = "244-0308"
        self.ruc = "179-005-3881003"
        self.cod_verificador = "79"
        self.aleatorio = str(random.randint(100,999))
        self.aleatorio1 = str(random.randint(100,999))
        self.aleatorio2 = str(random.randint(100,999))
        self.co = "CO - " + self.aleatorio
        self.fa = "FA - " + self.aleatorio1
        self.cr = "CR - " + self.aleatorio2
        self.productos = [["0","Taladro  ",39.99],
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
                          ["19","Martillo",6.25]]

    #Impresiones por parte de rubén 
    def factura(self):
        i = 0
        print("     ",self.titulo,"     ")
        print("RUC",self.ruc,"   ","DV",self.cod_verificador)
        print("Cod.",self.fa)
        print("Tel.",self.tel)
        print("------------------------------------------")
        print("Cliente: ",self.cliente)
        print("Código de pago: ",met_pagos.aux)
        print("Tipo de pago",tipo_pago.tipo_transaccion(met_pagos.aux))
        print("--------------  Compras  -----------------")
        print("Articulo        Cantidad      Precio      Subtotal")
        for i in range(len(ejecutar.carrito2)-1): 
            for z in ejecutar.carrito2: 
                print(z[i]) 
            print("") 
        print("------------------------------------------")
        print("ITBMS: 7%")
        print("Subtotal",self.subt)
        print("Porcentaje de descuento: ",calc.desc_porc)
        print("Descuento: ",round(calc.desc,2))
        print("Entregado: ",met_pagos.monto)
        print("Cambio: ",round(met_pagos.diferencia,2))
        print("-------------------------------------------")
        print("TOTAL: ",round(calc.total_compra,2))

    def compro_recibido(self):
        i = 0
        print("     ",self.titulo,"     ")
        print("RUC",self.ruc,"   ","DV",self.cod_verificador)
        print("Cod.",self.cr)
        print("Tel.",self.tel)
        print("------------------------------------------")
        print("Cliente: ",self.cliente)
        print("Código de pago: ",met_pagos.aux)
        print("Tipo de pago",tipo_pago.tipo_transaccion(met_pagos.aux))
        print("--------------  Compras  -----------------")
        print("Articulo        Cantidad      Precio      Subtotal")
        for i in range(len(ejecutar.carrito2)-1): 
            for y in ejecutar.carrito2: 
                print(y[i]) 
            print("") 
        print("------------------------------------------")
        print("ITBMS: 7%")
        print("Subtotal",self.subt)
        print("Porcentaje de descuento: ",calc.desc_porc)
        print("Descuento: ",round(calc.desc,2))
        print("Entregado: ",met_pagos.monto)
        print("Cambio: ",round(met_pagos.diferencia,2))
        print("-------------------------------------------")
        print("TOTAL: ",round(calc.total_compra,2))

    def cotizacion_impresa(self):
        k = 0
        print("     ",self.titulo,"     ")
        print("RUC",self.ruc,"   ","DV",self.cod_verificador)
        print("Cod.",self.co)
        print("Tel.",self.tel)
        print("------------------------------------------")
        print("Cliente: ",self.cliente)
        print("--------------  Cotizaciones  -----------------")
        print("Articulo        Cantidad      Precio      Subtotal")
        for k in range(len(ejecutar.carrito2)-1): 
            for w in ejecutar.carrito2: 
                print(w[k])
            print("") 
        print("------------------------------------------")
        print("ITBMS: 7%")
        print("Subtotal",round(self.subt,2))
        print("-------------------------------------------")
        print("TOTAL: ",round(calc.total_compra,2))

    def cotizacion_producto(self):
        control = 0
        i = 0
        carrito = [None] * 100
        ejecutar.carrito2 = []
        while self.resp == 's' or self.resp == 'S':
            print("\n---------------------------------------------")
            seleccion = int(input("Teclee el indice del producto a llevar: "))
            if seleccion < 0 or seleccion > 19:
                print("Por favor, teclee el indice correcto!")
                self.cotizacion_producto()
            print(self.productos[seleccion][1], "Precio: ", self.productos[seleccion][2])
            cantidad = int(input("Cuántos productos desea llevar --> "))
            carrito[control] = [str(self.productos[seleccion][1]) + "            " + str(cantidad)+"     "+str(self.productos[seleccion][2])+"     "+str(round(self.productos[seleccion][2]*cantidad,2))]
            control = control + 1
            self.subt = self.subt + (self.productos[seleccion][2] * cantidad)
            print("\n-------------------------------------------------------------------------")
            print("Desea comprar otro producto?  (s/S) para cotizar     /     otra letra para terminar")
            self.resp = input("respuesta ----> ")
        for i in range(len(carrito)):
            if(carrito[i]!= None):
                ejecutar.carrito2.append(carrito[i])
        print("\n\nDesea comprar lo cotizado?")
        print("(s/S) para Sí   /   otra letra para No")
        preg_cot1 = input("respuesta --->  ")
        calc.calcular_compras(self.subt,preg_cot1)
        if preg_cot1 == 's' or preg_cot1 == 'S':
            print("\n")
            met_pagos.menu_pago()
            print("\n\n\n\n")
            self.factura()
            print("\n\n\n")
            self.compro_recibido()
            print("\n\n\n")
            self.cotizacion_impresa()
        else:
            self.cotizacion_impresa()

    def cotizacion(self):
        i = 0
        j = 0
        print("\n----------------------------------")
        cli = input("Ingrese nombre del cliente: ")
        self.cliente = cli
        print("----------------------------------\n")
        for i in range(20):
            for j in range(3):
                print(self.productos[i][j],end="     \t\t")
            print("")
        self.cotizacion_producto()

    def compra_prod(self):
        control = 0
        i = 0
        vect_prod = []
        carrito = [None] * 100
        ejecutar.carrito2 = []
        while self.resp == 's' or self.resp == 'S':
            print("\n---------------------------------------------")
            seleccion = int(input("Teclee el indice del producto a llevar: "))
            if seleccion < 0 or seleccion > 19:
                print("Por favor, teclee el indice correcto!")
                self.compra_prod()
            print(self.productos[seleccion][1], "Precio: ", self.productos[seleccion][2])
            cantidad = int(input("Cuántos productos desea llevar --> "))
            carrito[control] = [str(self.productos[seleccion][1]) + "            " + str(cantidad)+"     "+str(self.productos[seleccion][2])+"     "+str(round(self.productos[seleccion][2]*cantidad,2)) ,"\n"]
            control = control + 1
            self.subt = self.subt + (self.productos[seleccion][2] * cantidad)
            print("\n-------------------------------------------------------------------------")
            print("Desea comprar otro producto?  (s/S) para comprar     /     otra letra para pagar")
            self.resp = input("respuesta ----> ")
        for i in range(len(carrito)):
            if(carrito[i]!= None):
                ejecutar.carrito2.append(carrito[i])
        print("\n\nHa realizado una cotización anteriormente?")
        print("(s/S) para Sí   /   otra letra para No")
        preg_cot = input("respuesta --->  ")
        calc.calcular_compras(self.subt,preg_cot)
        met_pagos.menu_pago()
        print("\n")
        if preg_cot == 's' or preg_cot == 'S':
            self.factura()
            print("\n\n\n")
            self.compro_recibido()
            print("\n\n\n")
            self.cotizacion_impresa()
        else:
            self.factura()
            print("\n\n\n")
            self.compro_recibido()
            
    def compras(self):
        i = 0
        j = 0
        print("\n----------------------------------")
        cli = input("Ingrese nombre del cliente: ")
        self.cliente = cli
        print("----------------------------------\n")
        for i in range(20):
            for j in range(3):
                print(self.productos[i][j],end="     \t\t")
            print()
        self.compra_prod()

    def menu(self):
        print("----------------------------------")
        print("    Ferretería el Gran Almacen    ")
        print("----------------------------------")
        print("1. Realizar compra")
        print("2. Realizar cotización")
        print("3. Salir")
        opc = int(input("respuesta ---> "))
        if opc == 1:
            self.compras()
        elif opc == 2:
            self.cotizacion()
        elif opc == 3:
            print("Que tenga un buen día!!!")
            print("Vuelva pronto")
            time.sleep(2)
            clear()
            sys.exit(0)
        else:
            print("Por favor teclee un valor válido")
            time.sleep(2)
            clear()
            self.menu()

ejecutar = llamada_principal()
ejecutar.menu()      