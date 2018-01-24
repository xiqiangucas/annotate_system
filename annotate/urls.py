from django.conf.urls import url,include
from django.contrib import admin
from annotate import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^hotword_page/(?P<date_str>(\d{4}-\d{2}-\d{2}))$', views.hotword_page),
    url(r'^hotword_action_page/$', views.hotword_action,name='hotword_action'),

    # url(r'^index_action/$', views.index_action),
    # url(r'^home/$', views.home),
    # url(r'^form/$', views.form_test),
    # url(r'^search/$', views.form_action),
    # url(r'^js_test/$', views.js_test),
]