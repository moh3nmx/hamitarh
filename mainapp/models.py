from django.db import models
from django_jalali.db import models as jmodels


class SiteViews(models.Model):
    visitCount = models.IntegerField(default=0)
    # Date Restarts after every change
    dateStarted = jmodels.jDateField(auto_now_add=True, blank=True, null=True)
    lastVisit = jmodels.jDateTimeField(auto_now=True, blank=True, null=True,)

    def __str__(self):
        return str('بازدید صفحه اصلی سایت')

    class Meta:
        verbose_name = 'شمارنده'
        verbose_name_plural = 'بازدید های سایت'




