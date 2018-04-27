from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    nome = models.CharField(max_length=128)
    usuario = models.ManyToManyField(User, blank=True, related_name='usuarios')
    
    publica = 'Publica'
    privada = 'Privada'
    institucional = 'Institucional'

    TIPO_AGENDAS_CHOICES = (
        ('Publica', 'Pública'),
        ('Privada', 'Privada'),
        ('Institucional','Institucional')
    )
    tipo = models.CharField(max_length=14, choices=TIPO_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    dataHora = models.DateTimeField(blank=True, null=True)
    local = models.CharField(max_length=60)
    notas = models.TextField()
    agenda = models.ForeignKey(Agenda, null=True, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + "( " + self.agenda.nome + " )"


class Convite(models.Model):
    anfitriao = models.ForeignKey(User, null=True, blank=False, on_delete=models.PROTECT)
    aceitar = models.BooleanField(default=False)
    convidados = models.ManyToManyField(User, blank=True, related_name='convidados')
    compromisso = models.ForeignKey(Compromisso, null=True, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.anfitriao.username + " fez um convite para o evento " + self.compromisso.nome

