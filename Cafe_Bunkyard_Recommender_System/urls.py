from django.conf.urls import url
from django.contrib import admin
from app.views import add

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/', add, name='addcat'),
]
