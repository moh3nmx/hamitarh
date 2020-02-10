from django.contrib import admin
from .models import User, Subscriber, UserManager


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'projectCount', 'isInvestor', 'email', 'last_login')
    admin.site.disable_action('delete_selected')

    def projectCount(self, obj):
        return obj.advertisement_set.count()
    projectCount.short_description = 'تعداد طرح ها'

@admin.register(Subscriber)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'dateSubscribed')

    def dateSubscribed(self, obj):
        return str(obj.dateRegistered)[:-12].replace(' ', ' -> ')