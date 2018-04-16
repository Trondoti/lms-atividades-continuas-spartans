"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from core import views
from core import urls

urlpatterns = [
    path(r'^login/$', views.login, name="login"),
    path('', views.index, name=""),
    path('base/', views.templateBase, name="base"),
    path('novo-aluno/', views.novoAluno, name="novo-aluno"),
    path('cursos/', views.cursos, name="cursos"),
    path('detalhe-curso-ads/', views.detalheCursoADS, name="detalhe-curso-ads"),
    path('detalhe-curso-bd/', views.detalheCursoBD, name="detalhe-curso-bd"),
    path('detalhe-curso-jd/', views.detalheCursoJD, name="detalhe-curso-jd"),
    path('detalhe-disciplina-tecweb/', views.detalheDisciplinaTecweb, name="detalhe-disciplina-tecweb"),
    path('detalhe-disciplina-bd/', views.detalheDisciplinaBd, name="detalhe-disciplina-bd"),
    path('detalhe-disciplina-devops/', views.detalheDisciplinaDevops, name="detalhe-disciplina-devops"),
    path('formulario-curso/', views.formularioCurso, name="formulario-curso"),
    path('formulario-disciplina/', views.formularioDisciplina, name="formulario-disciplina"),
    path('formulario-matricula/', views.formularioMatricula, name="formulario-matricula"),
    path('index/', views.index, name="index"),
    path('painel-admin/', views.painelAdmin, name='painel-admin'),
    path('login/', views.login, name ='login'),
    path('detalhes_disciplina/', views.detalheDisciplina, name ='Detalhe_Disciplina'),
    path('detalhes_disciplina-Gest-Proj/', views.detalheDisciplinaGestProj, name ='Detalhe_Disciplina'),

]