"""EXERCÍCIO 03: Classificador de Clima
Peça para o usuário digitar como está o tempo ("sol", "chuva", "neve", "nublado"). 
Use if/elif/else para recomendar um equipamento ou roupa adequada para o clima 
digitado (ex: se "chuva", recomendar "Guarda-chuva")."""

print("Sol")
print("Chuva")
print("Neve")
print("Nublado")

tempo = input("Qual é o tempo ?") .lower()

if tempo == "sol":
    print("Use um chápeu.")

elif tempo == "chuva":
    print("Pegue um Guarda-Chuva.")

elif tempo == "neve":
    print("Use roupas quentes e botas.")

elif tempo == "nublado":
    print("Leve um Guarda-Chuva, pode ser que chova.")

else:
    print("Opção inváida.")
