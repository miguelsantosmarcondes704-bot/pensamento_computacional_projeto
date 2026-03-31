


print('\n === Sistema de Padaria === \n')

while True:
    print("1.Encomendar pedido")
    print("2.Peça seu delivery")
    print("3.Cardapio")
    print("4.Cancelar encomenda")
    print("5.Contato")
    print("6.Localização")
    print("7.Redes sociais")
    print("0.Sair")

    escolha_menu = input("\n Escolha uma opção: \n")

    if escolha_menu == '1':
        print("\nPara encomendar o pedido preencha os campos abaixo...\n")
        nome_cliente = input("\nDigite o seu nome:\n")
        telefone_cliente = input("\nDigite o seu telefone:\n ")
        print("\nPedido a caminho,Obrigado pela preferência!\n")

    elif escolha_menu == '2':
        print("\nDigite o seu endereço...\n")
        bairro = input("\nBairro:\n")
        rua = input("\nRua:\n")
        numero = input("\nNúmero da residência\n")
        print("\nPedido a caminho,Obrigado pela preferência!\n")

        

        # while true:
            
    if escolha_menu == '3':
        
        print("\n1.Bolos\n")
        print("2.Pizzas\n")
        print("3.Bebidas\n")
        print("4.Pães\n")

        if escolha_menu == '1': 
         print ("Bolo de laranja")
        print ("Bolo de chocolate")
        print ("Bolo de cenoura")
        print ("Bolo de limão")

    elif escolha_menu == '2':
           print ("Pizza Portuguesa")
           print ("Pizza quatro queijos")
           print ("Pizza de calabresa")

    if escolha_menu == '3':
           print("Refrigerantes")
           print("Cervejas")
           print("Sucos Naturais")

    elif escolha_menu == '4':
           print("Pão Francês")
           print("Pão de Banha")
           print("Pão italiano")
        # continue

    
   
    break 

else:
        print("\nOpção inválida, tente novamente.\n")
