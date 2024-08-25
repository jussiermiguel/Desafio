from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_consultas, name='lista_consultas'),
    path('<int:pk>/', views.detalhe_consulta, name='detalhe_consulta'),
    path('criar/', views.criar_consulta, name='criar_consulta'),
    path('<int:pk>/atualizar/', views.atualizar_consulta, name='atualizar_consulta'),
    path('<int:pk>/excluir/', views.excluir_consulta, name='excluir_consulta'),
]