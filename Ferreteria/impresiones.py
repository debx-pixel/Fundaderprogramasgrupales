
def factura(self):
        i = 0
        aux = 12
        desc_porc = "10%"
        monto = 0
        desc = 0
        total_compra = 0
        diferencia = 0
        tipo_pago = 12
        carrito2 = []
        print("     ",self.titulo,"     ")
        print("RUC",self.ruc,"   ","DV",self.cod_verificador)
        print("Cod.",self.fa)
        print("Tel.",self.tel)
        print("------------------------------------------")
        print("Cliente: ",self.cliente)
        print("Código de pago: ",aux)
        print("Tipo de pago",tipo_pago.tipo_transaccion(aux))
        print("--------------  Compras  -----------------")
        print("Articulo        Cantidad      Precio      Subtotal")
        for i in range(len(carrito2)-1): 
            for z in carrito2: 
                print(z[i]) 
            print("") 
        print("------------------------------------------")
        print("ITBMS: 7%")
        print("Subtotal",self.subt)
        print("Porcentaje de descuento: ",desc_porc)
        print("Descuento: ",round(desc,2))
        print("Entregado: ",monto)
        print("Cambio: ",round(diferencia,2))
        print("-------------------------------------------")
        print("TOTAL: ",round(total_compra,2))

def compro_recibido(self):
    i = 0
    aux = 12
    desc = 0
    diferencia = 0
    total_compra = 0
    desc_porc = "10%"
    monto = 0
    tipo_pago = 12
    carrito2 = []
    print("     ",self.titulo,"     ")
    print("RUC",self.ruc,"   ","DV",self.cod_verificador)
    print("Cod.",self.cr)
    print("Tel.",self.tel)
    print("------------------------------------------")
    print("Cliente: ",self.cliente)
    print("Código de pago: ",aux)
    print("Tipo de pago",tipo_pago.tipo_transaccion(aux))
    print("--------------  Compras  -----------------")
    print("Articulo        Cantidad      Precio      Subtotal")
    for i in range(len(carrito2)-1): 
        for y in carrito2: 
            print(y[i]) 
        print("") 
    print("------------------------------------------")
    print("ITBMS: 7%")
    print("Subtotal",self.subt)
    print("Porcentaje de descuento: ",desc_porc)
    print("Descuento: ",round(desc,2))
    print("Entregado: ",monto)
    print("Cambio: ",round(diferencia,2))
    print("-------------------------------------------")
    print("TOTAL: ",round(total_compra,2))

def cotizacion_impresa(self):
    k = 0
    carrito2 = []
    total_compra = 0
    print("     ",self.titulo,"     ")
    print("RUC",self.ruc,"   ","DV",self.cod_verificador)
    print("Cod.",self.co)
    print("Tel.",self.tel)
    print("------------------------------------------")
    print("Cliente: ",self.cliente)
    print("--------------  Cotizaciones  -----------------")
    print("Articulo        Cantidad      Precio      Subtotal")
    for k in range(len(carrito2)-1): 
        for w in carrito2: 
            print(w[k])
        print("") 
    print("------------------------------------------")
    print("ITBMS: 7%")
    print("Subtotal",round(self.subt,2))
    print("-------------------------------------------")
    print("TOTAL: ",round(total_compra,2))