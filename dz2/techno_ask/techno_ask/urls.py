from django.conf.urls import url
from questions.views import getpost , AboutView

urlpatterns = [
    url(r'^$', getpost)
]
