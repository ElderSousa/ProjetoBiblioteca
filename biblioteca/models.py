import uuid
from django.db import models

# Create your models here.
class Livro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=15)
    autor = models.CharField(max_length=30)
    isbn = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo

class Locador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    TIPOLOCADOR = (
        ('F', 'FUNCIONARIO'),
        ('A', 'ALUNO')
    )

    tipo_locador = models.CharField(max_length=1, choices=TIPOLOCADOR, blank=False, null=False, default='A')

    def __str__(self):
        return f'{self.nome}'

class Locacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    locador = models.ForeignKey(Locador, on_delete=models.CASCADE)
    PERIODO = (
        ('M', 'DIURNO'),
        ('T', 'VESPERTINO'),
        ('N', 'NOTURNO')
    )
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

    def __str__(self):
        return f'Locador: {self.locador} - Livro: {self.livro} '