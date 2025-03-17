
catalogo = {
    "produto Nº1": {"nome": "abacate", "preço": 29.90, "estoque": 50},
    "produto Nº2": {"nome": "maracuja", "preço": 99.90, "estoque": 30},
    "produto Nº3": {"nome": "banana", "preço": 150.00, "estoque": 20}
}

while True:
    acao = int(input(
        "Qual das ações você quer realizar?\n"
        "Ver lista de produtos: 1\n"
        "Cadastrar itens: 2\n"
        "Terminar sessão: 3\n"
        "Digite aqui: "
    ))
    print("-" * 50)
    if acao == 1:
        # Iterar sobre os produtos no catálogo
        for produto, detalhes in catalogo.items():
            print(f"Produto: {produto}")
            print(f"Nome: {detalhes['nome']}")
            print(f"Preço: R${detalhes['preço']:.2f}")
            print(f"Estoque: {detalhes['estoque']} unidades")
            print("-" * 50)
    elif acao == 2:
        # Cadastrar um novo produto
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        # Gerar uma chave única para o novo produto
        novo_produto = f"Nº{(len(catalogo)+1):06}"
        catalogo[novo_produto] = {"nome": nome, "preço": preco, "estoque": estoque, }

        print(f"Produto '{nome}' cadastrado com sucesso!")
        print("-" * 50)

    elif acao == 3:
        print("Sessão encerrada.")
        break

    else:
        print("Opção inválida. Tente novamente.")
