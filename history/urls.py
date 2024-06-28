from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('history/', (views.AboutBankView.as_view()), name='about'),
]