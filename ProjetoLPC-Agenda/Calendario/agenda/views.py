from django.http import HttpResponse
from .models import *


def todasAgendas(request):
    retorno = "<h1> Todas as agendas cadastradas </h1>"
    listaAgendas = Agenda.objects.all()
    for a in listaAgendas:
        retorno += '<br> Nome Agenda: {} <br> Agenda criada por: {} <br> Tipo Agenda: {} <br> <br> '.format(a.nome, a.usuario, a.tipo)
    return HttpResponse(retorno)

def get_userAgendas_byID(request, id):
    retorno = "<h1> Agendas públicas </h1>"
    listaAgendasPublicas = Agenda.objects.filter(tipo='Publica',usuario__id=id)
    for a in listaAgendasPublicas:
        retorno += '<br> Nome Agenda: {} <br> <br> '.format(a.nome)
    return HttpResponse(retorno)

def agendaInstitucional(request):
    retorno = "<h1> Todos os compromissos institucionais </h1>"
    listaCompromissosInstitucionais = Compromisso.objects.filter(agenda__tipo='Institucional')
    for c in listaCompromissosInstitucionais:
        retorno += '<br> Nome do compromisso: {} <br> <br> '.format(c.nome)
    return HttpResponse(retorno)


