from django.contrib import admin
from .models import SiteViews


@admin.register(SiteViews)
class SiteViewsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'visitCount', 'lastViewed')

    def lastViewed(self, obj):
        return str(obj.lastVisit)[:-12].replace(' ', ' -> ')

    def reset_views(self, request, queryset):
        for counter in queryset:
            # counter.visitCount = 0
            counter.save()
        self.message_user(request, 'Counters flushed successfully!')

    reset_views.short_description = 'Reset visitCount of selected counters'