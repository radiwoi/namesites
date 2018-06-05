from django.contrib import admin

from .models import *


# admin.site.register(GirlName)
# admin.site.register(BoyName)
# admin.site.register(PopularName)
# admin.site.register(Variant)
admin.site.register(Email)


@admin.register(BoyName)
class BoyNameAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "frequency",
        "meaning"
    ]
    change_list_template = "admin/api/boyname/change_list.html"


@admin.register(GirlName)
class GirlNamesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "frequency",
        "meaning"
    ]
    change_list_template = "admin/api/girlname/change_list.html"


@admin.register(PopularName)
class PopularNamesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "year",
        "position",
        "gender"
    ]
    clange_list_template = "admin/api/popularname/change_list.html"


@admin.register(Variant)
class VariantsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "language"
    ]
    clange_list_template = "admin/api/variant/change_list.html"
