from django.contrib import admin
from meusite.models import MeuSite


@admin.register(MeuSite)
class MenuSiteAdmin(admin.ModelAdmin):
    list_display = 'title',

    def has_add_permission(self, request):
        return not MeuSite.objects.exists()
    