class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print(f"Produto com código {codigo} removido do carrinho.")
                break

    def visualizar_carrinho(self):
        if self.produtos:
            print("Produtos no carrinho:")
            for produto in self.produtos:
                print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: {produto.preco}")
        else:
            print("O carrinho está vazio.")


class FilaDePedidos:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def processar_pedido(self):
        if self.pedidos:
            pedido = self.pedidos.pop(0)
            return pedido
        else:
            print("Não há pedidos na fila.")
            return None


class PilhaDePagamento:
    def __init__(self):
        self.pedidos_pagos = []

    def realizar_pagamento(self, pedido):
        self.pedidos_pagos.append(pedido)

    def processar_pagamentos(self):
        if self.pedidos_pagos:
            pedido = self.pedidos_pagos.pop()
            print(f"Realizando pagamento do pedido: {pedido}")
        else:
            print("Não há pedidos para pagamento na pilha.")

    def visualizar_pagamentos(self):
        if self.pedidos_pagos:
            for pedido in self.pedidos_pagos:
                print(pedido)
        else:
            print("Não há pedidos pagos na pilha.")


class Pedido:
    def __init__(self, produtos):
        self.produtos = produtos

# Exemplo de utilização do sistema

# Crie alguns produtos
produto1 = Produto(1, "Camiseta", 20.0)
produto2 = Produto(2, "Calça Jeans", 50.0)
produto3 = Produto(3, "placa", 20.0)
produto4 = Produto(4, "tijolo", 10.0)
produto5 = Produto(5, "pizza", 30.0)


# Crie um carrinho de compras e adicione produtos
carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)
carrinho.adicionar_produto(produto4)
carrinho.adicionar_produto(produto5)

# Crie uma fila de pedidos e adicione um pedido
fila_de_pedidos = FilaDePedidos()
pedido = Pedido([produto1, produto2, produto3, produto4, produto5])
fila_de_pedidos.adicionar_pedido(pedido)

# Processe o pedido e realize o pagamento
pedido_processado = fila_de_pedidos.processar_pedido()
if pedido_processado:
    pilha_de_pagamento = PilhaDePagamento()
    pilha_de_pagamento.realizar_pagamento(pedido_processado)

# Visualize os pedidos pagos
pilha_de_pagamento.visualizar_pagamentos()



#EXEMPLO REMOÇÃO DO CARRINHO: 
# Selecione o item que deseja remover pelo código
carrinho.visualizar_carrinho()
carrinho.remover_produto(2)
# imprime o carrinho pos remoção 
carrinho.visualizar_carrinho()

