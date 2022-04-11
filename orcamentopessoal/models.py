from tabnanny import verbose
from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')


class Cartao(models.Model):
    bandeira = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    vencimento = models.DateField()
    data = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.bandeira

    def get_vencimento(self):
        return self.vencimento.strftime('%d')

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')

    class Meta:
        verbose_name_plural = 'Cartões'



class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cartao = models.ForeignKey(Cartao, on_delete=models.DO_NOTHING, null=True, blank=True)
    parcela = models.PositiveIntegerField(null=True, blank=True)
    fixo = models.BooleanField(default=False)
    pago = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')
