from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('<int:pk>/', views.detalhe_aluno, name='detalhe_aluno'),
    path('criar/', views.criar_aluno, name='criar_aluno'),
    path('<int:pk>/atualizar/', views.atualizar_aluno, name='atualizar_aluno'),
    path('<int:pk>/excluir/', views.excluir_aluno, name='excluir_aluno'),
]
