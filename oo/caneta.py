class Caneta:
    modelo = 'BIC'
    cor = 'Preta'
    carga = '95%'
    ponta = 1.5
    tampada = True
    def rabiscar(self):
        if self.tampada == True:
            print('Rabiscando')
        else:
            print('A caneta está tampada!')
"""Maneira melhor abaixo de fazer caneta"""
class Caneta:
   def __init__(self, modelo='Bic', cor='Preta', carga='95%', ponta=1.5, tampada=True)
       self.modelo = modelo
       self.cor = cor
       self.carga = carga
       self.ponta = ponta
       self.tampada = tampada
    def rabiscar(self):
        """Nesse método vou inverter a ordem, pois se é verdade que está tampada,
            então ela não pode rabiscar"""
        if self.tampada == True:
            print('A caneta está tampada!')
        else:
            print('Rabiscando')