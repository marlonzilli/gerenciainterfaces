from interface import Interface

hostname = input ("Digite o nome do roteador:")
qtd_interfaces = input ("Digite a quantidade de interfaces:")

lista_interfaces=[hostname]
x=0
while x < int(qtd_interfaces):
    ip = input ("Digite o IP da interface FastEthernet"+ str(x) + ": ")
    ifX = Interface("FastEthernet" + str(x), str(ip))
    lista_interfaces.append(ifX.imprime())
    x=x+1

print(lista_interfaces)



