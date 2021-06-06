from django.contrib import admin
from riders.models import Rider

# Register your models here.


class RiderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'image'
    )


admin.site.register(Rider, RiderAdmin)
