from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateField()

    def __str__(self):
        return self.descricao

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        super(Receita, self).save(*args, **kwargs)
    


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

    def save(self, *args, **kwargs):
        self.bandeira = self.bandeira.upper()
        super(Cartao, self).save(*args, **kwargs)



class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super(Categoria, self).save(*args, **kwargs)


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super(Pessoa, self).save(*args, **kwargs)


class Despesa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cartao = models.ForeignKey(Cartao, on_delete=models.DO_NOTHING, null=True, blank=True)
    parcela = models.PositiveIntegerField(null=True, blank=True)
    fixo = models.BooleanField(default=False)
    pago = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        super(Despesa, self).save(*args, **kwargs)
