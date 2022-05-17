from django.contrib import admin

from .models import Category, Message, Reaction


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'category', 'user')
    list_display_links = ('id', 'title', )
    list_per_page = 10


class ReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'published')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Reaction, ReactionAdmin)

