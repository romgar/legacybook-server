from django.contrib import admin

from graveyard.models import Decedent

class DecedentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Decedent, DecedentAdmin)
