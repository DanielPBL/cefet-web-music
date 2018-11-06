from django.db import models

# Create your models here.
class Musico(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    numero_albuns = models.IntegerField(null=True)

    def __str__(self):
        return self.nome+ ' - Data nascimento: ' + str(self.data_nascimento) + ' - Nº de álbuns: ' + str(self.numero_albuns)

class EstiloMusical(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=255)
    ano_formacao = models.IntegerField()
    numero_albuns = models.IntegerField()
    estilo_musical = models.ForeignKey(EstiloMusical, null=True, on_delete=models.SET_NULL)
    musicos = models.ManyToManyField(Musico)

    def __str__(self):
        return self.nome + ' - Ano formação: ' + str(self.ano_formacao) + ' - Nº de álbuns: ' + str(self.numero_albuns)