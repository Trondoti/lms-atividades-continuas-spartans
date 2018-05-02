from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from contas.views import listarAlunos, inserirAluno, alterarAluno, deletarAluno
from contas.views import listarCoordenadores, inserirCoordenador, alterarCoordenador, deletarCoordenador

urlpatterns = [
    path('listaralunos/', listarAlunos, name='listaralunos'),
    path('inseriraluno/', inserirAluno, name='inseriraluno'),
    path('deletaraluno/<int:idaluno>/', deletarAluno, name='deletaraluno'),
    path("alteraraluno/<int:idaluno>/", alterarAluno, name="alteraraluno"),
    path('listarcoordenadores/', listarCoordenadores, name='listarcoordenadores'),
    path('inserircoordenador/', inserirCoordenador, name='inserircoordenador'),
    path('deletarcoordenador/<int:idcoordenador>/', deletarCoordenador, name='deletarcoordenador'),
    path("alterarcoordenador/<int:idcoordenador>/", alterarCoordenador, name="alterarcoordenador"),
]
