from django.urls.conf import path, re_path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    re_path(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]
