from django.contrib import admin
from apps.store.admin import ProductAdmin
from apps.store.models import Product
from apps.tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline


class TagInLine(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
