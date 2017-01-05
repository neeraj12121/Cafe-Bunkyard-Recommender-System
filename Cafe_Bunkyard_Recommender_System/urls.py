from django.conf.urls import url
from django.contrib import admin
from app.views import PostAdPage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^postad/', PostAdPage.as_view()),
]
