'''
CRUD

PADARIA






'''


print ('\n === Sistema de Padaria === \n')


#python , com bibliotecas.
print("1.Encomendar pedido")
print("2.Peça seu delivery")
print("3.Cardapio")
print("4.Cancelar encomenda")
print("5.Contato")
print("6.Localização")
print("7.Redes sociais")
print("0.Sair")



while True:

    escolha_menu = input("\n Escolha uma opção: ")
    if escolha_menu == '1':

        print("Encomendando pedido...")
        nome_cliente = input("Digite o nome do cliente:")
        telefone_cliente = input("Digite o telefone do cliente: ")


    elif escolha_menu == input '0' :
    
        print("Saindo sistema. Até logo!")  
    break


else:
    print("opção inválida.Por favor,tente novamente.")