from django.contrib import admin

from .models import *

admin.site.register(FlicknamnFooterText)
admin.site.register(PojknamnFooterText)


@admin.register(BoyName)
class BoyNameAdmin(admin.ModelAdmin):
    filter_horizontal = ('variants', 'popular', )
    search_fields = ('name', )
    list_display = [
        'name',
        'frequency',
        'meaning',
    ]
    change_list_template = 'admin/api/boyname/change_list.html'


@admin.register(GirlName)
class GirlNamesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'frequency',
        'meaning',
    ]
    change_list_template = 'admin/api/girlname/change_list.html'


@admin.register(PopularName)
class PopularNamesAdmin(admin.ModelAdmin):
    filter_horizontal = ('boy_names', 'girl_names', )
    list_display = [
        'year',
        'position',
    ]
    search_fields = ('boy_names__name', 'girl_names__name',)
    change_list_template = 'admin/api/popularname/change_list.html'


@admin.register(Variant)
class VariantsAdmin(admin.ModelAdmin):
    filter_horizontal = ('boy_names', 'girl_names',)
    list_display = [
        'name',
        'language',
    ]
    search_fields = ('name',)
    change_list_template = 'admin/api/variant/change_list.html'


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'domain',
        'date',
        'time'
    ]
