from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^all/', todasAgendas, name='all'),
    url(r'^agenda/usuario/([0-9]{1})/', get_userAgendas_byID),
    url(r'^compromisso/', agendaInstitucional, name="Institucional")
]