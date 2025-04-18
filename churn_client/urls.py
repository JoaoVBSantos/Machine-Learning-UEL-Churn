from django.urls import path
from .views import ChurnCreateView, ChurnListView

urlpatterns = [
    path('', ChurnCreateView.as_view(), name='cadastro'),
    path('listagem/', ChurnListView.as_view(), name='listagem'),
]
