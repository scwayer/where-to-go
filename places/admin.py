from django.contrib import admin

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ("image", "position")


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
