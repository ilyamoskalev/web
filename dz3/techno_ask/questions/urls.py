from django.conf.urls import url
from django.conf import settings
from . import views

import django.views.defaults


urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^hot/', views.hot, name='hot'),
               url(r'^tag/(?P<tag>\w+)/?$', views.questions_by_tag, name='questions_by_tag'),
               url(r'^question/(?P<id>\d+)/?$', views.question, name='question'),
               url(r'^login/', views.login, name='login'),
               url(r'^signup/', views.signup, name='signup'),
               url(r'^ask/', views.ask, name='ask'),
               url(r'^settings/', views.settings, name='settings'),
]