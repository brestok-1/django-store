from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'get_html_photo', 'category')
    list_display_links = ('name',)
    search_fields = ('name', 'description')

    def get_html_photo(self, object):  # object refers to an object of the women class
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=60 height = 60>')

    get_html_photo.short_description = 'Image'


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
