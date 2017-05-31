from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hot/', views.hot, name='hot'),
    url(r'^tag/(?P<tag>\S+)/?$', views.questions_by_tag, name='questions_by_tag'),
    url(r'^question/(?P<id>\d+)/?$', views.question, name='question'),
    url(r'^user/(?P<user>\w+)/?$', views.questions_by_user, name='questions_by_user'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^settings/', views.settings, name='settings'),
]
