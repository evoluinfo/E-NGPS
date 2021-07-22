from django.db import models


class Company(models.Model):
    __tablename__ = 'Company'

    company_name = models.CharField(verbose_name='Empresa' ,max_length=100)
    email = models.EmailField(verbose_name='E-Mail', max_length=100)
    phone = models.CharField(verbose_name='Telefone' ,max_length=15)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=18, unique=True)
    SIZE = (
        ('AT', 'ATIVO'),
        ('IN', 'INATIVO'),
        ('AR', 'AGUARDANDO RESPOSTA')
    )
    situation = models.CharField(verbose_name='Situação', max_length=2, choices=SIZE, unique=True)

    def __str__(self):
        return f"{self.id} - {self.company_name}"