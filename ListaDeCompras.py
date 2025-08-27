from itertools import count

lista_de_compras = []
counter_id = count(1)

def listaDeCompras():

    print("Bem-vindo à Lista de Compras")

    while True:

        print("\n\n--------------PRODUTOS----------------")
        for produto in lista_de_compras:
            mostrarProduto(produto)

        print("\n\n-------------MENU--------------")
        print("A. Adicionar produto")
        print("B. Remover produto")
        print("C. Pesquisar produtos")
        print("D. Sair do Programa\n\n")

        option = input("Selecione uma Opção: ").upper()

        if option == "A":
            adicionarProduto()

        elif option == "B":
            removerProduto()

        elif option == "C":
            pesquisarProdutos()

        elif option == "D":
            print("Muito obrigado por usar o programa!")
            break

        else:
            print("Opção Inválida, tente novamente.")
            continue

def adicionarProduto():
    print("--------Adicionando produtos--------")
    nome_produto = input("Nome do produto: ")
    print("Selecione a Unidade de Medida")
    print("A. Quilograma")
    print("B. Grama")
    print("C. Litro")
    print("D. Mililitro")
    print("E. Unidade")
    print("F. Metro")
    print("G. Centímetro")
    unidade_de_medida = input("Unidade de medida: ").upper()
    if unidade_de_medida in ["A", "B", "C", "D", "E", "F", "G"]:
        quantidade = input("Quantidade: ")
        descricao_do_produto = input("Descrição do produto: ")
        id = next(counter_id)

        lista_de_compras.append({
            "nome_produto": nome_produto,
            "quantidade": quantidade,
            "unidade_de_medida": unidadeDeMedida(unidade_de_medida),
            "descricao_do_produto": descricao_do_produto,
            "id": id
        })

    else:
        print("unidade inválida, tente novamente.")

def unidadeDeMedida(unidade_de_medida):
    if unidade_de_medida == 'A':
        resultado = 'Quilograma'
    elif unidade_de_medida == 'B':
        resultado = 'Grama'
    elif unidade_de_medida == 'C':
        resultado = 'Litro'
    elif unidade_de_medida == 'D':
        resultado = 'Mililitro'
    elif unidade_de_medida == 'E':
        resultado = 'Unidade'
    elif unidade_de_medida == 'F':
        resultado = 'Metro'
    elif unidade_de_medida == 'G':
        resultado = 'Centímetro'
    return resultado

def removerProduto():
    print("------------Remover produto-------------")
    id_pesquisado = int(input("Id do produto: "))
    encontrado = False
    for i in lista_de_compras:
        if i['id'] == id_pesquisado:
            lista_de_compras.remove(i)
            print("Produto removido com sucesso!")
            encontrado = True
    if not encontrado:
        print("id inválido ou não encontrado")

def pesquisarProdutos():
    encontrado = False
    print("--------Pesquisar produtos--------")
    nome_pesquisado = input("Informe o nome do produto: ").lower()
    for produto in lista_de_compras:
        if nome_pesquisado in produto['nome_produto'].lower():
            mostrarProduto(produto)
            encontrado = True
    if not encontrado:
        print("Produto não encontrado")

def mostrarProduto(produto):
    print("Nome do produto: ", produto['nome_produto'])
    print("Unidade de Medida: ", produto['unidade_de_medida'])
    print("Quantidade: ", produto['quantidade'])
    print("Descrição do produto: ", produto['descricao_do_produto'])
    print("ID: ", produto['id'], "\n")

listaDeCompras()