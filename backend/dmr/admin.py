from django.contrib import admin
from .models import DailyReading, Outfall


# Register your models here.
class DailyReadingAdmin(admin.ModelAdmin):
    list_display = ("date", "outfall", "flow", "gallons")


class OutfallAdmin(admin.ModelAdmin):
    list_display = ("number", "description")


admin.site.register(DailyReading, DailyReadingAdmin)
admin.site.register(Outfall, OutfallAdmin)
