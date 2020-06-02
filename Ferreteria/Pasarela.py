from os import system, name
import time
import sys
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class PaymentGateway:
    def __init__(self):
        self.dicct = {"Error":500,"message":"Esta no es una tarjeta permitida"}
        self.dicc  = {"Error":500,"message":"Esto no es una transacción permitida"}
        self.montx = "Es monto no es permitido"
        self.resp = 's'
        self.t_trans = ""
        self.creditc = ""
        self.transs = 0
        self.cadena = ""
        self.inicial_aux = ""
        self.tarjeta = ""
        self.montos1 = 0
        self.aux = 0
        self.visa = "Visa"
        self.Mas = "MasterCard"
        self.Ae = "American Express"
        self.a = "Auth"
        self.c = "Capture"
        self.s = "Sale"

    def trans_aux(self,tipotrans):
        if tipotrans.lower() == "auth":
            self.transs = self.auth()
        elif tipotrans.lower() == "capture":
            self.transs = self.capture()
        elif tipotrans.lower() == "sale":
            self.transs = self.sale()
        else:
            return 1

    def auth(self):
        return self.a

    def capture(self):
        return self.c
    
    def sale(self):
        return self.s

    def tarjeta_aux(self,inicial):
        self.inicial_aux = inicial
        if self.inicial_aux[0] == '4':
            self.tarjeta = "Visa"
        elif self.inicial_aux[0] == '5':
            self.tarjeta = "MasterCard"
        elif self.inicial_aux[0] == '6': 
            self.tarjeta = "American Express"
        else:
           return 2

        aux = len(inicial)
        x = aux - 4
        self.cadena ="**********" + inicial[x:aux]

    # def monto_aux(self, cantidad,auxiliar,limite):
    #     if auxiliar == 12: 
    #         if cantidad < 1 or cantidad > 150000.00:
    #             return 3
    #         else:
    #             self.montos1 = cantidad
    #     elif auxiliar == 13:
    #         print()
    
    def transaccion(self):
        print("--------------------------------")
        print("      Tipo de transacción       ")
        print("--------------------------------")
        print("transacciones: (auth / capture / sale)")
        print("Teclee el tipo de transacción a realizar")
        self.t_trans1 = input("Aquí --> ")
        t_trans = self.t_trans1
        self.trans_aux(t_trans)
        aux = self.trans_aux(t_trans)
        if aux == 1:
            print("\n",self.dicc)
            print("Regresando...")
            time.sleep(2)
            self.transaccion()
        
    def tarjeta_ingreso(self):
        print("Debe iniciar con: (4 / 5 / 6)")
        print("\nIngrese su número de tarjeta")
        self.creditc = input("Aquí --> ") 
        num_tarjeta = self.creditc
        self.tarjeta_aux(num_tarjeta)
        aux2 = self.tarjeta_aux(num_tarjeta)
        if aux2 == 2:
            print(self.dicct)
            print("Regresando...")
            time.sleep(2)
            self.tarjeta_ingreso()
            
    def montos(self):
        print("\nIngrese el monto de transacción")
        print("================================")
        self.monto = float(input("monto --> "))
        cant_monto = self.monto
        self.monto_aux(cant_monto)
        aux3 = self.monto_aux(cant_monto)
        if aux3 == 3:
            print(self.montx)
            print("Regresando...")
            time.sleep(2)
            self.montos()

    def imprimir(self):
        self.do_sale()

# ejecutar = PaymentGateway()
# ejecutar.transaccion()
# ejecutar.tarjeta_ingreso()
# ejecutar.montos()
# ejecutar.imprimir()