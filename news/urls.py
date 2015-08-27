from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^account/login$', views.login, name='login'),
    url(r'^account/$', views.loggedin, name='loggedin'),
    url(r'^account/register$', views.register, name='register'),
    url(r'^account/loggedout$', views.logout, name='logout'),
    url(r'^all/$', views.articles, name='articles'),
    url(r'^get/(?P<article_id>[0-9]+)/$', views.article, name='article'),
    url(r'^media/$', views.media, name='media'),
]