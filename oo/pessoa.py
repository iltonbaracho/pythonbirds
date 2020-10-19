class Pessoa:
    olhos = orelhas = 2
    nariz = boca = 1

    def __init__(self, nome=None, idade=0):
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return f'Pessoa({self.nome}, {self.idade})'

    @classmethod
    def atributos_da_classe(cls):
        return f'Olhos: {cls.olhos}, Orelhas: {cls.orelhas}, Nariz: {cls.nariz}, Boca: {cls.boca}'


print(Pessoa.atributos_da_classe())
p = Pessoa('Wagner', 31)
print(p)