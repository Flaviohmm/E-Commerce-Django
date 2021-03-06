from django.urls.conf import re_path

from . import views

app_name = 'account'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^alterar-dados/$', views.update_user, name='update_user'),
    re_path(r'^alterar-senha/$', views.update_password, name='update_password'),
    re_path(r'^registro/$', views.register, name='register'),
]