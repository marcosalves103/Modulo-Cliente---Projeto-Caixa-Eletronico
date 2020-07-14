import os
import time

def menu():
    
    while True:
        time.sleep(2)
        os.system("cls")
        print("======== MENU CLIENTE =======")
        print("1 - Cadastrar Banco ou Fintech")
        print("2 - Alterar Banco ou Fintech")
        print("3 - Listar Bancos e Fintechs")
        print("4 - Excluir Banco ou Fintech")
        print("5 - Sair do Sistema de Cliente")
        print("="*28)
        try:
            opcao = int(input("Digite o opção desejada: "))
            if 1 <= opcao <= 5:
                if opcao == 1:
                    cadastro()
                elif opcao == 2:
                    print("Não programado ainda.")
                elif opcao == 3:
                    print("Não programado ainda.")
                elif opcao == 4:
                    print("Não programado ainda.")
                else:
                    print("Saindo do Programa...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Êxito em sair do programa.")
                    break
            else:
                print("A entrada não pertence a uma das opções.")
        except:
            print("A entrada não é válida.")

def cadastro():
    
    funcionalidades = [ "Todas abaixo", "Saque", "Depósito","Extrato","Transferência (DOC e TED)","Pagamento","Bloquear cartão","Investimentos (Rendas fixa ou variável)","Conta corrente","Conta poupança","Conta com aplicação de seu dinheiro em uma renda fixa","Renegociação de dívidas","Cheques","Comprovante (de transferência, pagamento e recarga de celular)","Empréstimo","Crédito no celular","Crédito imobiliária","Seguros","Troca por milhas","Gerente Virtual","Abrir Conta (por meio de bot ou tela chamada com o responsável); "] 
    print(" ")
    print("==== CADASTRO =====")
    print(" ")
    input("Digite o CNPJ da empresa: ")
    print("...")
    time.sleep(2)
    print("Data de abertuta: 00/00/0000")
    print("nome da empresa: XXXX")
    print("nome fantasia: XXXX")
    print("código de descrição da natureza juridica: XXXX")
    print("="*28)
    input("Localização da sede (CEP): ")
    print("bairro: XXXX")
    print("Cidade: XXXX")
    print("Lougradouro: XXXX")
    print("="*28)
    input("Digite a inscrição estadual: ")
    print("="*28)
    print("FUNCIONALIDADES DISPONIVEIS...")
    time.sleep(2)
    for i in range(len(funcionalidades)):
        time.sleep(0.1)
        print("{} - {}".format(i,funcionalidades[i])) 
    print(" ")
    input("Digite os numeros correspondentes as funcionalidades que deseja oferecer aos seus clientes (separado por virgula):")
    print("...")
    time.sleep(2)
    print("="*28)
    input("Todas as informações foram inseridas, deseja finalizar o cadastro agora?(S/N) :")
    time.sleep(2)
    print("Cadastro finalizado com sucesso!")
    time.sleep(3)
    print("IMPRIMINDO...")
    time.sleep(3)
    

menu()