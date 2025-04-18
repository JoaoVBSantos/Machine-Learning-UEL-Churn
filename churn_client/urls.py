from django.contrib import admin
from django.urls import path
from .views import prever_churn, lista_registros, editar_registro, dados_churn, dados_contrato, dados_pagamento, dashboard



urlpatterns = [
    path('', prever_churn, name='prever_churn'),
    path('registros/', lista_registros, name='lista_registros'),
    path('editar/<str:pk>/', editar_registro, name='editar_registro'),
    path('dados_churn/', dados_churn, name='dados_churn'),
    path('dados_contrato/', dados_contrato, name='dados_contrato'),
    path('dados_pagamento/', dados_pagamento, name='dados_pagamento'),
    path('dashboard/', dashboard, name='dashboard'),
]