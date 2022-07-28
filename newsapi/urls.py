from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('china/',views.china, name='china'),
    path('united-arab-emirates/',views.uae, name='uae'),
    path('argentina/',views.argentina, name='argentina'),
    path('austria/',views.austria, name='austria'), 
    path('australia/',views.australia, name='australia'),
    path('belgium/',views.belgium, name='belgium'),     
]