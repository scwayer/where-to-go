from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ("image", "get_preview", "position")

    readonly_fields = ["get_preview"]

    def get_preview(self, instance):
        resize_coefficient = instance.image.width / 300 if instance.image.width > 300 else 1
        return format_html('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=instance.image.url,
            width=instance.image.width / resize_coefficient,
            height=instance.image.height / resize_coefficient
        ))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#
#     readonly_fields = ["get_preview"]
#
#     def get_preview(self, instance):
#         return format_html('<img src="{url}" width="{width}" height="{height}" />'.format(
#             url = instance.image.url,
#             width = instance.image.width,
#             height = instance.image.height
#         ))


# admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
