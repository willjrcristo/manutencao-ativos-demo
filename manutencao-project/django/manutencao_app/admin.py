from django.contrib import admin
from .models import Ativo, ManutencaoProgramada, OrdemServico

admin.site.register(Ativo)
admin.site.register(ManutencaoProgramada)
admin.site.register(OrdemServico)