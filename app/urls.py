from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login.html$',views.login,name="login"),
    url(r'^register.html$', views.register,name="register"),
    #url(r'^logout.html$', views.logout, name="logout"),



]
