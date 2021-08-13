from django.db import models


class Seller(models.Model):

    __tablename__ = "Client"

    company_name = models.CharField(verbose_name='empresa', max_length=100)
    responsible = models.CharField(verbose_name='responsável', max_length=100)
    department = models.CharField(verbose_name='setor', max_length=50)
    email = models.EmailField(verbose_name='email', max_length=200)
    phone = models.CharField(verbose_name='telefone', max_length=20)
    city = models.CharField(verbose_name='cidade', max_length=20)
    SIZE = (
        ("SP", 'São Paulo'),
        ("PR", 'Paraná'),
        ("SC", 'Santa Catarina'),
        ("RS", 'Rio Grande do Sul')
    )
    state = models.CharField(verbose_name='estado', choices=SIZE, max_length=30)
    modality = models.CharField(verbose_name='modalidade', max_length=40)
    n_service = models.PositiveBigIntegerField(verbose_name='n° serviços')
    price = models.FloatField(verbose_name='preço')
    avarage_billing = models.FloatField(verbose_name='faturamento médio')
    contract_anniversary = models.DateField(verbose_name='contrato aniversário')
    proposal = models.DateField(verbose_name='proposta', blank=True)
    historic = models.TextField(verbose_name='histórico', blank=True)
    date_created = models.DateTimeField(verbose_name='criação', auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='atualização', auto_now=True)

    def __str__(self) -> str:
        return f"{self.company_name} - {self.responsible} - {self.department} -\
                 {self.email} - {self.phone} - {self.city} - {self.state} - \
                 {self.modality} - {self.n_service} - {self.price} - \
                 {self.avarage_billing} - {self.contract_anniversary} - {self.proposal} - \
                 {self.historic} - {self.date_created} - {self.date_update}"