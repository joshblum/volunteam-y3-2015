from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib import auth

from app import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^login/$', views.loginPage, name='login'),
    url(r'^login2/$', auth.views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^volunteam/$', views.volunteam, name='volunteam'),
    url(r'^signup2/$', views.signupRequest, name='signup'),
    url(r'^showUsers/$', views.showUsers, name='Show users'),
    url(r'^events/$', views.events, name='Events'),
)

