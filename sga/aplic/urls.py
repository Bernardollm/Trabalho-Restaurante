from django.urls import path
from django.conf.urls.static import static
from .views import IndexView
from .views import CardapioView
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cardapio', CardapioView.as_view(), name='cardapio'), 

]


