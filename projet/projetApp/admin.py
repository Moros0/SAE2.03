from django.contrib import admin

from .models import Machine , Personnel , Reseau

# Register your models here.

admin.site.register(Machine)
admin.site.register(Personnel) #ces trois lignes permettent de gérer depuis la page admin les trois modèles
admin.site.register(Reseau)