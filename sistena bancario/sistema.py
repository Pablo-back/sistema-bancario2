from datetime import datetime, date, time, timedelta
import textwrap

def menu():
    menu = """ \n
    ============ Menu ============
    [d]\tDepositar
    [s]\tSacar
    [i]\tExtrato
    [nc]\tNoca Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    =======================
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("Deposito realizado com sucesso")
    
    else:
        print("Sua operação falhou")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, nmero_saque, limite_saque):
    if saldo > 0:
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = nmero_saque > limite_saque
    
    elif excedeu_limite:
        print("Você não tem mais limite!")
    
    elif excedeu_saque:
        print("O seu numero de saque acabou por hoje.")

    elif excedeu_saldo:
        print("Voce esta sem saldo")

    elif saldo > 0:
        saldo -= valor
        extrato += f"Saque> R${valor:.2f}\n"
        nmero_saque += 1
        print("Saque realizado com sucesso")

    else:
        print("Operação falhou.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Digite seu cpf(somento numeros)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("Já existe um usuario com esse cpf.")
        return
    
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: (Apenas numeros.)")
    endereço = input("Digite a cidade que voce mora.")

    usuarios.append({"nome=": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereço": endereço})

    print("Usuario criado com sucesso.")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe seu CPF(Apenas numero.)")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Usuario criado com sucesso")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("usuario não encontrado. Fluxo de criação de conta encerrada.")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C\C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['none']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []

    while True:
        opcao = menu()
        

        if opcao == "d":
            valor = float(input("Informe o valor que voce quer depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor que voce quer sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                nmero_saque=numero_saques,
                limite_saque=LIMITE_SAQUE,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuario)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuario)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas.append(contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalida!")

main()