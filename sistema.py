def deposito():
    global saldo
    depositado = float(input("Qual o valor do depósito? "))
    saldo = saldo + depositado
    
    msg_extrato = f"""
    ----------
    Depósito realizado
    Valor = R$:{depositado}
    Saldo atual = R$: {saldo}
    """
    global extratar
    extratar = extratar + msg_extrato
    print(saldo)

def saque():
    global saldo, numero_saque, LIMITE_SAQUE
    if(numero_saque < LIMITE_SAQUE):
        saque = int(input("Qual o valor do saque? "))
        if(saldo > saque):
            saldo = saldo - saque
            numero_saque += 1
            msg_extrato = f"""
     ----------
    Saque realizado
    Valor = R$:{saque}
    Saldo atual = R$: {saldo}
            """
            global extratar
            extratar = extratar + msg_extrato
        else:
            print("Saldo insuficiente para o saque")

    else:
        print("Impossível fazer essa operação - Limite de transações excedidas")

def extrato():
    global extratar
    print(extratar)


mensagem = """
Bem vindo ao sistema Bancário Dio!
Digite a operação que você deseja realizar:
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair
"""
saldo = 0
numero_saque = 0
valor_limite = 500
LIMITE_SAQUE = 3
operacao = -1
extratar = " --- Banco DIO ---"
while True:
    operacao = int(input(mensagem))
    if(operacao == 1):
        deposito()
    elif(operacao == 2):
        saque()
    elif(operacao == 3):
        extrato()
    elif(operacao == 0):
        print("Operação finalizada")
        break
    else:
        print("Opção inválida")