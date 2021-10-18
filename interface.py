class Interface:
    def __init__(self, nome, ip):
        self.nome = nome
        self.ip = ip

    def update(self):
        self.nome = input ("Informe a interface:")
        self.ip = input ("Informe o IP:")

    def imprime(self):
        return (self.nome + ":" + self.ip)







