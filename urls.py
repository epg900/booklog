from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('editlog/', views.editlog, name='editlog' ),
    path('deletelog/', views.deletelog, name='deletelog' ),    
]

