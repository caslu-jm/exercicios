"""EXERCÍCIO 04: Caixa Eletrônico Infinito                                                              
Crie uma variável saldo = 1000. Inicie um loop while True que mostra um menu: 
1 - Ver Saldo, 2 - Sacar, 3 - Depositar, 4 - Sair. Use if/elif/else para as opções.
- Se escolher Sacar, peça o valor e use um if/else aninhado para garantir que o 
  valor não é maior que o saldo.
- Se escolher Sair, quebre o loop com break."""

saldo = 1000.0

while True:
    print("Bem vindo ao caixa.")
    print("1- Ver saldo.")
    print("2- Sacar.")
    print("3- Depositar dinheiro.")
    print("4- Sair.")

    opcao = input("Escolha uma opção.")

    if opcao == "1":
        print(f"Seu saldo é {saldo} R$")
    elif opcao == "2":
        saque = float(input("Digite o valor de saque: "))
        if saque <= 0:
            print("Valor inválido")
        elif saque > saldo:
            print("Valor indesponível.")
        saldo = saldo - saque
    elif opcao == "3":
        deposito = float(input("Digite o valor do deposito: "))
        if deposito <= 0:
            print("Valor Inválido.")
        saldo = saldo + deposito
    elif opcao == "4":
        print("Encerrando sistema...")
        break
    else:
        print("Operador Inválido.")

