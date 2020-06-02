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