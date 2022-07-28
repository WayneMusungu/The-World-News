from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('china/',views.china, name='china'),
    path('united-arab-emirates/',views.uae, name='uae')
    
]