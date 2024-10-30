from django.contrib import admin
from blog.models import Account, Projects, Messages


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'rezyume']
    list_display_links = ['id', 'user']

    def has_add_permission(self, request):
        return False


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'url', 'url_name', 'image', 'created_at']
    list_display_links = ['id', 'user']


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

