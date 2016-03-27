from django.contrib import admin
# Register your models here.
from apps.base.models import News, Follower


class FollowerAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')


admin.site.register(News)
admin.site.register(Follower, FollowerAdmin)
