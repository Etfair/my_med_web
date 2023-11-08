from django.contrib import admin

from main.models import Category, Service, Comment, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'content', 'category', 'image', 'view_count',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'create_at', 'service',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'create_at', 'view_count',)
