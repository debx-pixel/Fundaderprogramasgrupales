class metodo_pagos:
    def __init__(self):
        self.diferencia = 0
        self.monto = 0
        self.cuenta = 400

    def pago(self):
        print("Teclee el monto a pagar: ")
        self.monto = float(input("---> "))
        if self.monto > self.cuenta:
            self.diferencia = self.monto - self.cuenta
        else:
            print("Dinero insuficiente...")
            print("Volviendo...")
            self.pago()
    
    def tarjeta(self):
        #pasarela_tarjeta.transaccion()
        #pasarela_tarjeta.tarjeta_ingreso()
        print("Teclee el monto a pagar: ")
        self.monto = float(input("---> "))
        if self.monto > self.cuenta:
            self.diferencia = self.monto - self.cuenta
        else:
            print("Dinero insuficiente...")
            print("Volviendo...")
            self.tarjeta()
    
    def enlinea(self):
        if self.cuenta > 1000.00:
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
            self.menu()
            
met_pagos = metodo_pagos()