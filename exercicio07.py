import math

#entrada
raio = float(input("Digite o valor do raio da circunferência: "))


#processamento
area = math.pi * (raio ** 2)
perimetro = 2 * math.pi * raio

#saida
print("A área da circunferência é:", area)
print("O perímetro da circunferência é:", perimetro)

