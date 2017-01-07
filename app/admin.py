from django.contrib import admin
from app.models import menu


class MenuAdmin(admin.ModelAdmin):
    list_display = [ "item", "price"]

    class Meta:
        model = menu

admin.site.register(menu, MenuAdmin)