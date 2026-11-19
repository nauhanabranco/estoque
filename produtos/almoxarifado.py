# Classe responsável por administrar o almoxarifado.

class Almoxarifado:
    # Construtor: cria um almoxarifado vazio.
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []

    # Adiciona um produto à lista do almoxarifado.
    def adicionar(self, produto):
        self.produtos.append(produto)
            # Procura um produto pelo seu código.
    def buscar(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None
        # Registra a entrada de produtos no estoque.
    def entrada(self, codigo, qtd):
        produto = self.buscar(codigo)
        if produto:
            produto.entrada(qtd)
            return True
        return False
        # Registra a saída de produtos do estoque.
    def saida(self, codigo, qtd):
        produto = self.buscar(codigo)
        if produto:
            return produto.saida(qtd)
        return False
        # Lista todos os produtos do almoxarifado.
    def listar(self):
        return [produto.listar_produtos() for produto in self.produtos]
        # Identifica os produtos que precisam de reposição.
    def solicitacao_compra(self):
        return [
            produto.listar_produtos()
            for produto in self.produtos
            if produto.situacao() in ["Repor", "Em falta"]
        ]
        # Calcula o valor total dos produtos em estoque.
    def valor_estoque(self):
        return sum(
            produto.preco * produto.quantidade
            for produto in self.produtos
        )
        # Transforma os dados do almoxarifado em um dicionário.
        # Transforma os dados do almoxarifado em um dicionário.
    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "produtos": self.listar(),
            "total_produtos": len(self.produtos),
            "valor_total": self.valor_estoque()
        }