from django.contrib import admin
from serviciosapp.models import Servicios
# Register your models here.

class serviciosAdmin(admin.ModelAdmin):
    list_display=("titulo","contenido", "created","update","imagen")
    search_fields=("titulo","contenido")
    list_filter=("created","update")

admin.site.register(Servicios, serviciosAdmin)

