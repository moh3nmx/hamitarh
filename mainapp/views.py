from django.shortcuts import render, redirect
from ads.models import AdCategory, Advertisement, Slide
from django.http import Http404, HttpResponse
from .models import SiteViews
from zeep.client import Client



def index(request):
    # Views Count
    if not request.user.is_superuser:
        count = SiteViews.objects.all()[0]
        count.visitCount += 1
        count.save()
    return render(request, 'mainapp/index.html', {
        'top3': Advertisement.objects.filter(isBest=True)[::-1],
        'cats_list': AdCategory.objects.all(),
        'inProgress': Advertisement.objects.filter(fundingStep__isnull=False).__len__(),
        'isPresented': Advertisement.objects.filter(isPresented=True).__len__(),
        'ads_list': Advertisement.objects.filter(containInSlideshow=True)[::-1],
        'Slides': Slide.objects.all(),
    })


def blog(request):
    return render(request, 'mainapp/blog.html')


def verify(request):
    return render(request, 'mainapp/750790.txt')


def intro(request):
    return render(request, 'mainapp/intro.html')


