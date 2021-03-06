from django.conf.urls import url
from django.contrib.auth.views import login, logout
from zhihu import views
app_name = 'zhihu'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^index/$', views.index, name='index'),
    url(r'^active/(?P<token>(.*))/$', views.active, name='active'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^post_question/(?P<id>[0-9]+)/$',
        views.post_question, name='post_question'),
    url(r'^create_question/$', views.create_question, name='create_question'),
    url(r'^personal/$', views.personal, name='personal'),
    url(r'^forget_pwd/$', views.forget_pwd, name='forget_pwd'),
    url(r'^reset_pwd/$', views.reset_pwd, name='reset_pwd'),
]
