from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_html_photo')
    list_display_links = ('username',)
    search_fields = ('username', 'email')

    def get_html_photo(self, object):  # object refers to an object of the women class
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=60 height = 60>')

    get_html_photo.short_description = 'Image'


admin.site.register(User, UserAdmin)
