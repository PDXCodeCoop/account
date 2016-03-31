from django.conf.urls import patterns, url

from . import views

urlpatterns = [
               url(r'^$', views.profile_private, name='account'),
               url(r'^register$', views.register, name='register'),
               url(r'^logout$', views.logout_view, name='logout'),
               url(r'^login$', views.login_view, name='login'),
               url(r'^social$', views.login_social, name='login_social'),
               url(r'^profile$', views.profile_private, name='profile'),
               url(r'^public/(?P<username>[^\.]+)/$', views.profile_public, name='public'),
               
               ]
