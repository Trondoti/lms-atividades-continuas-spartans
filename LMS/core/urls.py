from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.index),
    path ('base/', views.templateBase),
    path ('novoaluno/', views.novoAluno),
    path ('cursos/', views.cursos),
    path ('detalhe-curso/', views.detalheCurso),
    path ('detalhe-disciplina/', views.detalheDisciplina),
    path ('formulario-curso/', views.formularioCurso),
    path ('formulario-disciplina/', views.formularioDisciplina),
    path ('formulario-matricula/', views.formularioMatricula),
    path ('index/', views.index),
]