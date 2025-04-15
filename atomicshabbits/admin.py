from django.contrib import admin

from atomicshabbits.models import Habbits


# Register your models here.
@admin.register(Habbits)
class HabbitsAdmin(admin.ModelAdmin):
    list_display = ('action', 'time', 'periodicity', 'connected_habbit', 'award')
    list_filter = ('is_public',)
