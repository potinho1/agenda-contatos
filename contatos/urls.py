from django.urls import path

from . import views

urlpatterns = [
    path('', views.contatos_list_view, name='contatos_list_view'),
    path('editar/<int:contato_id>/', views.editar_contato, name='editar_contato'),
    path('novo-grupo/', views.novo_grupo_view, name='novo_grupo'),
    path('<int:contato_id>/novo_tel/', views.novo_tel_view, name='novo_tel'),
    path('<int:contato_id>/novo_email/',
         views.novo_email_view, name='novo_email'),
]
