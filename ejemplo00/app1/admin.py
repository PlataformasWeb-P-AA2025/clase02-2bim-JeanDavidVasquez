from django.contrib import admin

# IMportar las clases del modelo.

from app1.models import Estudiante
admin.site.register(Estudiante)

from app1.models import ciudad
admin.site.register(ciudad)