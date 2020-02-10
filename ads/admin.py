from django.contrib import admin
from .models import AdCategory, Advertisement, State, Investor, Slide
from jalali_date.admin import ModelAdminJalaliMixin

from SarmayeTemp.settings import MEDIA_ROOT

import os
import csv

from jalali_date import date2jalali
# Register your models here.


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('title', 'investor_advertisement_count', 'isBig')

    def investor_advertisement_count(self, obj):
        return obj.advertisement_set.count()
    investor_advertisement_count.short_description = 'تعداد طرح ها'

    filter_horizontal = ('interest', 'user')


@admin.register(AdCategory)
class AdCategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'visitCount', 'lastViewed')

    def lastViewed(self, obj):
        return str(obj.lastVisit)[:-12].replace(' ', ' -> ')


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'link', 'title')


@admin.register(Advertisement)
class AdsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'owner', 'Fund', 'fundingStep', 'jrequestDate', 'showInSite',
                    'isBest',
                    'isPaid',
                    'isReviewed',
                    'isReviewOK', 'isInvited', 'isInterviewOK', 'isPresented', 'isContracted')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': (('title', 'fund'), 'category', ('owner', 'phone'), ('creator', 'location'), 'summary')
        }),
        ('اطلاعات اضافی', {
            'fields': (('proposal', 'images'), ('executiveSummary', 'fundUsage', 'estimatedCosts'), 'presentIncome',
                       'damage', 'benefitShare', 'rateOfReturn', 'compet', 'presentCustomers', 'marketingPlan',
                       'marketSize',
                       'resume', 'investorShare', 'revenueModel', ('expected_gain', 'expected_time'))
        }),
        ('دسترسی ها', {
            'fields': (('showInSite', 'containInSlideshow'), )
        }),
        ('مراحل جذب سرمایه', {
            'fields': (('fundingStep', 'requestDate'), ('review', 'isReviewOK'), 'report', ('isInvited', 'InvitationDate'),
            'interviewReport', 'isInterviewOK',
                       ('isPresented', 'investor'), 'isContracted')
        }
        )
    )
    filter_horizontal = ('investor',)
    list_filter = ('showInSite', 'category', 'location', )
    search_fields = ('title', 'owner')
    list_editable = ('showInSite', 'isBest')

    def jrequestDate(self, obj):
        if obj.requestDate:
            return str(date2jalali(obj.requestDate)).replace('-', '/')
        else:
            return '-'

    jrequestDate.short_description = 'تاریخ آخرین درخواست'

    def Fund(self, obj):
        try:
            return format(int(obj.fund), ",d")
        except:
            return obj.fund
    Fund.short_description = 'سرمایه'

    def reset_request(self, request, queryset):
        for ad in queryset:
            ad.fundingStep = None
            ad.requestDate = None
            ad.isReviewOK = False
            ad.review.delete()
            ad.save()
        self.message_user(request, "Reset was successful.")

    reset_request.short_description = 'پاک کردن درخواست'

    def export_csv(self, request, queryset):
        with open(os.path.join(MEDIA_ROOT, 'HamitarhProjects.csv'), 'w', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'presentIncome', 'fund', 'resume', 'rateOfReturn', 'compet', 'marketSize', 'credits']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for a in queryset:
                writer.writerow({'title': a.title, 'presentIncome': a.presentIncome, 'fund': a.fund, 'resume': a.resume,
                                 'credits': a.credits,
                                 'rateOfReturn': a.rateOfReturn, 'compet': a.compet,
                                 'marketSize': a.marketSize,
                                 })

        self.message_user(request, "Exported Successfully")

    export_csv.short_description = 'خروجی اکسل'

    def reset_views(self, request, queryset):
        for ad in queryset:
            ad.visitCount = 0
            ad.save()
        self.message_user(request, "VisitCoutns successfully flushed.")

    reset_views.short_description = 'پاک کردن آمار بازدید'

    def get_actions(self, request):
        # Disable delete
        actions = super(AdsAdmin, self).get_actions(request)
        if 'delete_selected' in admin.site.actions:
            admin.site.disable_action('delete_selected')
        return actions

    actions = [reset_views, reset_request, 'delete_selected', export_csv]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('title', 'state_advertisement_count')

    def state_advertisement_count(self, obj):
        return obj.advertisement_set.count()
    state_advertisement_count.short_description = 'تعداد طرح ها'

