"""EXERCÍCIO 01: Calculadora Direta
Peça ao usuário dois números e um operador matemático (+, -, *, /). 
Use a estrutura if/elif/else no operador para realizar a conta e exibir o 
resultado. Inclua um else no final para exibir "Operador inválido".
"""
operador = input("Digite o operador da calculadora (+,-,*,/): ")

numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))

if operador == "+":
    print("Resultado: ", numero1 + numero2)

elif operador == "-":
    print("Resultado: ", numero1 - numero2)

elif operador == "*":
    print("Resultado: ", numero1 * numero2)

elif operador == "/":
    print("Resultado: ", numero1 * numero2)

else:
    print("Resultado inválido")