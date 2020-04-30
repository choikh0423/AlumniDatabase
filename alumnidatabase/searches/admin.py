from django.contrib import admin
from .models import Alumni
from .models import College
from .models import Major
from .models import Industry
from .models import Location
from .models import Employer
from .models import Profile

# Register your models here.

admin.site.register(College)
admin.site.register(Major)
admin.site.register(Industry)
admin.site.register(Location)
admin.site.register(Employer)


@admin.register(Alumni)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'college', 'graduation_date',
                    'industry', 'current_employer')


admin.site.register(Profile)
