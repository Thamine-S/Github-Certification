#operação de dois números solicitados 
numero_1 = float(input("insira número: "))
numero_2 = float(input("insira número:"))
operacao = input("""
    qual operação deseja executar?
            digite "/" -> divisão
            digite "*" -> multiplicação
            digite "+" -> soma
            digite "-" -> subtração
            digite "**" -> potenciação
    sua resposta: """)

if operacao == "/":
    divisao = numero_1 / numero_2
    print(f"{numero_1} / {numero_2} = {divisao}")
elif operacao == "*":
    divisao = numero_1 * numero_2
    print(f"{numero_1} * {numero_2} = {divisao}")
elif operacao == "+":
    soma = numero_1 + numero_2 
    print(f"{numero_1} + {numero_2} = {soma}")
elif operacao == "-":
    subtracao = numero_1 - numero_2
    print(f"{numero_1} - {numero_2} = {subtracao}")
elif operacao == "**":
    potencia = numero_1 ** numero_2 
    print(f"{numero_1} ** {numero_2} = {potencia}")
else:
    print("Operação inválida.")