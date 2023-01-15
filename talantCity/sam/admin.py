from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu, Article


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class MenuAdmin(CustomMPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(
    Menu,
    MenuAdmin,
)

admin.site.register(
    Article,
)

