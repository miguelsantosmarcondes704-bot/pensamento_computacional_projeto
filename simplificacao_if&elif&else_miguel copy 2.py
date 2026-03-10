print('Qual a sua idade?')


idade = int(input())

if idade < 18:
    print('Voce é menor de idade')

elif idade <= 18:
    print('Voce é adulto')

else:
    print('Voce é idoso de idade')

    preco_frutas = {
        'maçã': 2.5,
        'banana': 1.8,
        'laranja': 3.0
    }

    fruta_desejada = 'maçã'


    resultado = preco_frutas.get(fruta_desejada, 'Fruta não encontrada')

    print(f"O preço da {fruta_desejada} é R${resultado}")   