from django.contrib import admin
from . forms import DynpageForm
from . models import DynPage


@admin.register(DynPage)
class DynPageAdmin(admin.ModelAdmin):
    form = DynpageForm
    fieldsets = (
        ('Required settings', {
            'fields': ('url', 'language',)
        }),
        ('Required meta', {
            'fields': ('title', 'description', 'keywords',)
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Advanced settings', {
            'classes': ('collapse',),
            'fields': ('template_name',),
        }),
    )
    list_display = ('url', 'title', 'language')
    search_fields = ('url', 'title')