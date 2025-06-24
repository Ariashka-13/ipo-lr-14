from django.urls import path
from .views import index, author, lamps

urlpatterns = [
    path('', index, name='index'),
    path('author', author, name='author'),
    path('lamps', lamps, name='lamps'),
]