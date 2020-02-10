from django.db import models
from django.core.urlresolvers import reverse
from authentication.models import User
from django_jalali.db import models as jmodels
from datetime import datetime
from jalali_date import date2jalali

from ckeditor.fields import RichTextField


class AdCategory(models.Model):
    url = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=200)

    def CatImage_directory_path(obj, filename):
        return 'CatImage/cat{0}-{1}-{2}'.format(obj.id, obj.title, filename)
    icon = models.ImageField(upload_to=CatImage_directory_path, blank=True)
    # number of person who visit the Cat
    visitCount = models.IntegerField(default=0, null=True, verbose_name='Visit Count')
    lastVisit = jmodels.jDateTimeField(auto_now=True, blank=True, null=True, verbose_name='Last Viewed by User')

    def get_url(self):
        return reverse('show_cat', args=(self.url, ))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class State(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class Investor(models.Model):
    # Investor title
    title = models.CharField('عنوان', max_length=40, blank=True, null=True)

    def InvestorLogo_directory_path(obj, filename):
        return 'InvestorLogo/{0}/{1}'.format(obj.title, filename)

    logo = models.ImageField('لوگو', upload_to=InvestorLogo_directory_path, blank=True)

    isBig = models.BooleanField('سرمایه گذار بزرگ', default=False)

    interest = models.ManyToManyField(AdCategory, verbose_name='علاقه مندی ها')

    description = models.TextField('درباره سرمایه گذار', max_length=700, blank=True, null=True)

    commentAboutUs = models.TextField('پیام برای حامی طرح', max_length=700, blank=True, null=True)

    country = models.CharField('کشور', max_length=100, blank=True, null=True)

    user = models.ManyToManyField(User, verbose_name='نماینده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سرمایه گذار'
        verbose_name_plural = 'سرمایه گذاران'


class Advertisement(models.Model):
    # TODO: make a Form instead!
    # TODO: date and time correction!
    # title of Advertisement
    title = models.CharField(max_length=400, verbose_name='عنوان')
    # category of Advertisement
    category = models.ForeignKey(AdCategory, null=True, verbose_name='دسته بندی')
    # The User who creates the Ad
    creator = models.ForeignKey(User, null=True, verbose_name='کاربر')
    # The Owner of Ad (maybe the creator)
    owner = models.CharField(max_length=30, null=True, verbose_name='صاحب طرح')
    # Owner's Phone
    phone = models.CharField(max_length=30, null=True, verbose_name='شماره تماس')
    # how much is needed to run
    fund = models.CharField(max_length=50, null=True, verbose_name='مبلغ سرمایه')
    # expected gain
    expected_gain = models.CharField('سود پیش‌بینی شده', max_length=5, null=True, blank=True)
    # in expected time
    expected_time = models.CharField('زمان پیش‌بینی شده', max_length=5, null=True, blank=True)
    # number of person who visit the Ad
    visitCount = models.IntegerField(default=0, null=True, verbose_name='بازدید')
    # city
    location = models.ForeignKey(State, null=True, verbose_name='استان')
    # some details (2-3 lines)
    summary = models.TextField(blank=True, verbose_name='شرح')
    # paid amount
    paidAmount = models.IntegerField(blank=True, null=True, verbose_name='مبلغ پرداخت شده')
    # Verify user ads by admin
    showInSite = models.BooleanField(default=False, verbose_name='نمایش')
    # is in homepage slide show ?
    containInSlideshow = models.BooleanField(default=True, verbose_name='نمایش در اسلاید')
    # credits about Ad
    credits = models.TextField('نحوه ضمانت', max_length=200, blank=True, default='')
    # Natural Person or Legal Person
    isLegal = models.BooleanField(default=False)

    isReviewed = models.BooleanField('نقد شده', default=False)


    # Optional Fields
    executiveSummary = models.TextField('خلاصه اجرایی طرح', max_length=1000, blank=True, default='')

    fundUsage = models.TextField('نحوه استفاده از سرمایه جذب شده', max_length=1000, blank=True, default='')

    presentIncome = models.TextField('درآمد سالیانه', max_length=1000, blank=True, default='')

    resume = models.TextField('سابقه کاری', max_length=1000, blank=True, default='')

    investorShare = models.TextField('درصد مشارکت سرمایه گذار', max_length=1000, blank=True, default='')

    estimatedCosts = models.TextField('هزینه های پیش بینی شده', max_length=1000, blank=True, default='')

    revenueModel = models.TextField('مدل درآمدی', max_length=1000, blank=True, default='')

    marketSize = models.TextField('اندازه بازار', max_length=1000, blank=True, default='')

    marketingPlan = models.TextField('برنامه بازاریابی', max_length=1000, blank=True, default='')

    presentCustomers = models.TextField('مشتریان فعلی', max_length=1000, blank=True, default='')

    compet = models.TextField('مزیت رقابتی', max_length=1000, blank=True, default='')

    rateOfReturn = models.TextField('نرخ بازگشت سرمایه', max_length=1000, blank=True, default='')

    benefitShare = models.TextField('نحوه تقسیم سود', max_length=1000, blank=True, default='')
    # damages
    damage = models.TextField('زیان‌دهی', max_length=1000, blank=True, default='')


    # TODO: should handle multi images !
    def AdImage_directory_path(obj, filename):
        return 'AdImage/user_{0}/ad{1}-{2}'.format(obj.creator.phone, obj.id, filename)
    images = models.ImageField(upload_to=AdImage_directory_path, blank=True)
    # TODO: should handle multi files ! and format Validation

    def AdFile_directory_path(obj, filename):
        return 'AdFile/user_{0}/ad{1}-{2}'.format(obj.creator.phone, obj.id, filename)
    proposal = models.FileField('پروپوزال', upload_to=AdFile_directory_path, blank=True, null=True)

    dateCreated = models.DateTimeField('تاریخ ثبت', auto_now_add=True, blank=True, null=True)

    lastModified = models.DateTimeField(auto_now=True, blank=True)

    # TODO: Add a Date for Updating ads !

    FUNDING_STEPS = [
        ('0', 'نقد و بررسی'),
        ('1', 'جلسه حضوری'),
        ('2', 'معرفی به سرمایه گذار'),
        ('3', 'عقد قرارداد'),
    ]

    # is Qualified?
    fundingStep = models.CharField('آخرین درخواست', max_length=30, choices=FUNDING_STEPS, blank=True, null=True)

    # Request Date (Date of Changing step)
    requestDate = models.DateField('تاریخ آخرین درخواست', blank=True, null=True)

    def review_directory_path(obj, filename):
        return 'AdReview/ad_{0}/{1}__{2}'.format(obj.id, date2jalali(datetime.today()).strftime('%y_%m_%d'),filename)
    review = models.FileField('فایل نقد', upload_to=review_directory_path, blank=True, null=True)

    # Report
    report = RichTextField(null=True, blank=True, verbose_name='گزارش نقد')
    # Paid for review
    isPaid = models.BooleanField(default=False, verbose_name='پرداخت')
    # Evaluated (barchasbe taeed!)
    isReviewOK = models.BooleanField(default=False, verbose_name='تایید نقد')
    # Invite for Interview
    isInvited = models.BooleanField(default=False, verbose_name='دعوت به جلسه')
    # Interview Date
    InvitationDate = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ جلسه')
    # :)
    isInterviewOK = models.BooleanField(default=False, verbose_name='تایید جلسه')

    interviewReport = RichTextField(null=True, blank=True, verbose_name='گزارش جلسه')

    isPresented = models.BooleanField(default=False, verbose_name='معرفی به سرمایه گذار')

    investor = models.ManyToManyField(Investor, blank=True, verbose_name='سرمایه گذار')

    isContracted = models.BooleanField(default=False, verbose_name='عقد قرارداد')

    isBest = models.BooleanField('بهترینها', default=False)

    def get_url(self):
        return reverse('show_ad', args=(str(self.id)))

    def __str__(self):
        return self.title[:10] + '...' if self.title.__len__() > 15 else self.title

    class Meta:
        verbose_name = 'طرح'
        verbose_name_plural = 'طرح ها'

    def save(self, *args, **kwargs):
        super(Advertisement, self).save(*args, **kwargs)
        if self.review:
            self.isReviewed = True
            super(Advertisement, self).save(*args, **kwargs)
        for i in self.investor.all():
            for u in i.user.all():
                u.isInvestor = True
                u.save()


class Slide(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان')
    link = models.URLField(blank=True, null=True)

    def SlideImage_directory_path(obj, filename):
        return 'SlideImage/P{0}/{1}'.format(obj.id, filename)

    image = models.ImageField('تصویر', upload_to=SlideImage_directory_path, blank=True)
    content = RichTextField('متن', config_name='default')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدها'

#
#
# class LocationRegion(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return 'Location: ' + self.name
#
# #
# class CapitalNeedAdvertisement(Advertisement):
#     capitalNeedMin = models.IntegerField()
#     capitalNeedMax = models.IntegerField()
#     owner = models.CharField(max_length=200)
#     ownerType = models.IntegerField(choices=ownerTypes)
#     estimatedProfit = models.IntegerField(blank=True)
#     estimatedMonths = models.IntegerField(blank=True)
#     locations = models.ManyToManyField(LocationRegion)
#
#     def __str__(self):
#         return 'CapitalNeed' + super(CapitalNeedAdvertisement, self).__str__()

