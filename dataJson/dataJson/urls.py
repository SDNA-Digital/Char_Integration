"""
URL configuration for dataJson project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Dash_IncidenteArea 
from .views import Dash_Politicas_Manuais
from .views import Dash_Norma
from .views import Dash_RadarConformidade
from .views import Dash_Processo
from .views import Card_Processos
from .views import Dash_ProcessoxArea
from .views import Dash_PlanosMitigantes
from .views import Tabela_Tarefas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dash_IncidenteArea/', Dash_IncidenteArea),
    path('Dash_Politicas_Manuais/', Dash_Politicas_Manuais),
    path('Dash_Normas/', Dash_Norma),
    path('Dash_RadarConformidade/', Dash_RadarConformidade),
    path('Dash_Processo/', Dash_Processo),
    path('Card_Processos/', Card_Processos),
    path('Dash_ProcessoxArea/', Dash_ProcessoxArea),
    path('Dash_PlanosMitigantes/', Dash_PlanosMitigantes),
    path('Tabela_Tarefas/', Tabela_Tarefas),
]