
#objetivo: Calcular IMC e Classificar de forma simples

nome = input("nome: ")
peso = float (input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)  #aritméticos
print (f"IMC de {nome} : {imc:.2f}")


#comparação + lógicos (faixa simplificada)
baixo_peso = imc < 18.5
normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc >= 25) and (imc < 30)
obesidade = imc >= 30

print("Baixo peso?", baixo_peso)
print("normal?", normal)
print("Sobrepeso?", sobrepeso)
print("Obesidade?", obesidade)

