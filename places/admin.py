from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    fields = ("my_order", "image", "get_preview")

    readonly_fields = ["get_preview"]

    def get_preview(self, instance):
        resize_coefficient = instance.image.width / 300 if instance.image.width > 300 else 1
        return format_html('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=instance.image.url,
            width=instance.image.width / resize_coefficient,
            height=instance.image.height / resize_coefficient
        ))


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):

    readonly_fields = ["get_preview"]

    def get_preview(self, instance):
        resize_coefficient = instance.image.width / 300 if instance.image.width > 300 else 1
        return format_html('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=instance.image.url,
            width=instance.image.width / resize_coefficient,
            height=instance.image.height / resize_coefficient
        ))
