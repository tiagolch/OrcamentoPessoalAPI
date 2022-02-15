from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')