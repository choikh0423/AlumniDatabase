from django.contrib import admin
from .models import Alumni

# Register your models here.


@admin.register(Alumni)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'graduation_date',
                    'industry', 'current_employer')
