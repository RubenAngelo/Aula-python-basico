from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

print(caminhao_rosa)
print(type(caminhao_rosa))
print(caminhao_rosa.cor)
print(caminhao_rosa.rodas)
print(caminhao_rosa.marca)
print(caminhao_rosa.tanque)

carro_azul = Carro('azul', 'bmw', 30)

print(carro_azul.cor)
print(carro_azul.rodas)
print(carro_azul.marca)
print(carro_azul.tanque)

carro_azul.abastecer(10)
print(carro_azul.tanque)
carro_azul.abastecer(70)
print(carro_azul.tanque)