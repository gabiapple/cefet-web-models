from django.db import models

# Create your models here.
class Musico(models.Model):
    nome = models.CharField(max_length=80)
    instrumento = models.CharField(max_length=50)
    AMADOR = 'Amador'
    PROFISSIONAL = 'Profissional'

    EXPERIENCIA_CHOICES = (
        (AMADOR, 'Amador'),
        (PROFISSIONAL, 'Profissional'),
    )

    experiencia = models.CharField(
        max_length=2,
        choices=EXPERIENCIA_CHOICES,
        default=AMADOR,
    )

    def __str__(self):
        return "{} | {} | {}".format(self.nome, self.instrumento, self.experiencia)


class EstiloMusical(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome


class Banda(models.Model):
    nome = models.CharField(max_length=80)
    sigla = models.CharField(max_length=6)
    estilo = models.ForeignKey(EstiloMusical, on_delete=models.PROTECT)
    musicos = models.ManyToManyField(Musico)

    def __str__(self):
        return self.nome