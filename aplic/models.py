from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def str(self):
        return self.nome

class Prato(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='pratos/', blank=True, null=True)
    disponivel = models.BooleanField(default=True)

    def str(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField()

    def str(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em preparação', 'Em preparação'),
        ('Pronto', 'Pronto'),
        ('Entregue', 'Entregue'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pratos = models.ManyToManyField(Prato, through='PedidoPrato')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')

    def str(self):
        return f'Pedido #{self.id} - {self.cliente.nome}'

class PedidoPrato(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def str(self):
        return f'{self.quantidade}x {self.prato.nome} no pedido {self.pedido.id}'