"""EXERCÍCIO 02: Menu de Jogo Arcade
Crie um menu inicial com as opções: 1 - Novo Jogo, 2 - Carregar Jogo, 
3 - Configurações, 4 - Sair. Use if/elif/else para ler a escolha do usuário 
e imprimir uma mensagem correspondente (ex: "Iniciando nova partida...").
"""
print("=====MENU ARCADE=====")
print("Novo Jogo")
print("Carregar Jogo")
print("Configurações")
print("Sair")

opcao = input("Insira a opção desejada: ")

if opcao == "Novo Jogo":
    print("Carregando Jogo...")

elif opcao == "Carregar Jogo":
    print("Entrando no Save...")

elif opcao == "Configurações":
    print("Abrindo Menu...")

elif opcao == "Sair":
    print("Saindo do Game...")

else:
    print("Opção invalida.")


