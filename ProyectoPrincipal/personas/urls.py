from django.urls import URLPattern, path

from .views import persona

urlpatterns = [

    path('', persona, name='persona')
]