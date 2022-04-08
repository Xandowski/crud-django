from django.urls import path

from .views import index

app_name = 'app.core'

urlpatterns = [
    path('', index, name='index'),
]
