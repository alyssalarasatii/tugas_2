# TODO: Implement Routings Here
from django.urls import path
from katalog.views import s_katalog

app_name = 'katalog'

urlpatterns = [
    path('', s_katalog, name='s_katalog'),
]