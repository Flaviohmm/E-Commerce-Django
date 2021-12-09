from django.conf.urls import url
from . import views

app_name = 'catalog'

urlpatterns = [
    url('', views.product_list, name='product_list'),
]
