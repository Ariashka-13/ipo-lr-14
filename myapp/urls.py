from django.urls import path
from . import views

urlpatterns = [
    path('spec/', views.spec_list, name='spec_list'),  
    path('spec/<int:id>/', views.spec_detail, name='spec_detail'),  
]