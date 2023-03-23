# Fazer uma calculadora; dado dois valores e um operador a saída deve ser o resultado da operação

while True:
    validade_num = not None

    try:
        valor_1  = input("Digite um número: ")
        valor_2  = input("Digite outra número: ")
        operador = input("Qual operação você deseja realizar, +, *, -, /? ")
        valor_1_float  = float(f'{valor_1}')
        valor_2_float  = float(f'{valor_2}')
    except:
        validade_num = None
    
    
    if validade_num == None:
        print("Você não digitou valores válidos")
        print("-"*100)
        continue

    operadores_permitidos = "/*-+"
    
    if operador not in operadores_permitidos:
        print("Digite um operador válido")
        continue
    
    if len(operador) > 1:
        print("Digite um único operador")
        continue

    if operador   == "+":
        resultado = valor_1_float + valor_2_float
        print(f"O valor de {valor_1_float} + {valor_2_float} é {resultado}")
    elif operador == "-":
        resultado = valor_1_float - valor_2_float
        print(f"O valor de {valor_1_float} - {valor_2_float} é {resultado}")
    elif operador == "*":
        resultado = valor_1_float * valor_2_float
        print(f"O valor de {valor_1_float} * {valor_2_float} é {resultado}")
    elif operador == "/":
        resultado = valor_1_float / valor_2_float
        print(f"O valor de {valor_1_float} / {valor_2_float} é {resultado}")
    

    resposta_da_pessoa = input("Você deseja sair? [S] ou [s] ").lower().startswith("s")
    
    if resposta_da_pessoa:
        print("Você saiu da calculadora")
        break
    print("-"*100)