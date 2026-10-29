from produto import Produto

p1 = Produto() #Criação do objeto 1 (produto 1)
p1.nome = "Macarrão parafuso"
p1.quantidade = 5

p2 = Produto() #Criação do objeto 2 (produto 2)
p2.nome = "Molho de tomate"
p2.quantidade = 3

print(f"{p1.nome}: {p1.quantidade} un")
print(f"{p2.nome}: {p2.quantidade} un")