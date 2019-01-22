from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Houses, Train

# Register your models here.
@admin.register(Houses)
class HousesAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Train)
