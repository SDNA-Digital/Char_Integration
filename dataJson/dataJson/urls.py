from .views import Card_Processos
from .views import Dash_ProcessoxArea
from .views import Dash_PlanosMitigantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dash_IncidenteArea/', Dash_IncidenteArea),
    path('Dash_Politicas_Manuais/', Dash_Politicas_Manuais),
    path('Dash_Normas/', Dash_Norma),
    path('Dash_RadarConformidade/', Dash_RadarConformidade),
    path('Dash_Processo/', Dash_Processo),
    path('Card_Processos/', Card_Processos),
    path('Dash_ProcessoxArea/', Dash_ProcessoxArea),
    path('Dash_PlanosMitigantes/', Dash_PlanosMitigantes)
]