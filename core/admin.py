from django.contrib import admin

from core.models import *


class DoujinshiImageInline(admin.TabularInline):
    model = DoujinshiImage
    extra = 10


class DoujinshiAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', 'serie')
    inlines = (DoujinshiImageInline, )


admin.site.register(Doujinshi, DoujinshiAdmin)
admin.site.register(Auteur)
admin.site.register(Serie)
admin.site.register(Tag)
