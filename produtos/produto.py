# Classe Produto do back-end do almoxarifado

class Produto:
    # Construtor: recebe os quatro dados do produto
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    # Informa a situação do estoque
    def situacao(self):
        if self.quantidade == 0:
            return "Em falta"
        elif self.quantidade <= 4:
            return "Repor"
        else:
            return "OK"

    # Devolve os dados em um dicionário
    def listar_produtos(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "situacao": self.situacao(),
        }

    # Adiciona unidades ao estoque
    def entrada(self, qtd):
        self.quantidade = self.quantidade + qtd

    # Retira unidades se houver estoque suficiente
    def saida(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade = self.quantidade - qtd
            return True
        return False