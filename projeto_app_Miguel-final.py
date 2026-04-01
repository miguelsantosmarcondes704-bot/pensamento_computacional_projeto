


print('\n === Sistema de Padaria === \n')

while True:
    print("1.Encomendar pedido")
    print("2.Peça seu delivery")
    print("3.Cardapio")
    print("4.Contato")
    print("5.Localização")
    print("6.Redes sociais")
    print("0.Sair")

    escolha_menu = input("\n Escolha uma opção: \n")

    if escolha_menu == '1':
        print("\nPara encomendar o pedido preencha os campos abaixo...\n")
        nome_cliente = input("\nDigite o seu nome:\n")
        telefone_cliente = input("\nDigite o seu telefone:\n ")
        print("\nPedido a caminho,Obrigado pela preferência!\n")

        escolha_menu == input ("Sair:")

        if escolha_menu == '0':
             break

    elif escolha_menu == '2':
        print("\nDigite o seu endereço...\n")
        bairro = input("\nBairro:\n")
        rua = input("\nRua:\n")
        numero = input("\nNúmero da residência\n")
        print("\nPedido a caminho,Obrigado pela preferência!\n")

        escolha_menu == input ("Sair:")

        break

        

    while True:
            
     if escolha_menu == '3':

        print("1.Bolos\n")
        print("2.Pizzas\n")
        print("3.Bebidas\n")
        print("4.Pães\n")

        escolha_menu == input("\nEscolha uma opção:")
        
        if escolha_menu == '0':
          print("Saindo até logo:3\n")
        
        break

        if escolha_menu == '1': 
        
            print ("Bolo de laranja")
        print ("Bolo de chocolate")
        print ("Bolo de cenoura")
        print ("Bolo de limão")

        escolha_menu == input ("\nSair:")

    if escolha_menu == '2':
           print ("Pizza Portuguesa")
           print ("Pizza quatro queijos")
           print ("Pizza de calabresa")
           
           escolha_menu == input ("\nSair:")

    elif escolha_menu == '3':
           print("Refrigerantes")
           print("Cervejas")
           print("Sucos Naturais")
           
           escolha_menu == input ("\nSair:")

    elif escolha_menu == '4':
           print("Pão Francês")
           print("Pão de Banha")
           print("Pão italiano")
           
           escolha_menu == input ("\nSair:")
  

else:
        print("\nOpção inválida, tente novamente.\n")  


