from django.contrib import admin
from django.urls import path
from base.views import *

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('fale_conosco/', fale_conosco, name='fale_conosco'),
    path('admin/', admin.site.urls),
]
