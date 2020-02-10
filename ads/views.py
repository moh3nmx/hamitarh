from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from .models import AdCategory, Advertisement
from django.db.models import F
from authentication.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


# All Users
def show_ad(request, adID):
    """ Shows a certain ad with unique """
    ad = get_object_or_404(Advertisement, id=adID)
    # ad visit count - self visit
    if not request.user.is_superuser:
        ad.visitCount += 1
        ad.save()
    if ad.showInSite or ad.creator == request.user:
        return render(request, 'mainapp/show_ad.html', {
            'ad': ad,
        })
    raise Http404


# Premium Users
def show_ad_premium(request, adID):
    """ Shows a certain ad with unique """
    ad = get_object_or_404(Advertisement, id=adID)
    # ad visit count - self visit
    if not request.user.is_superuser:
        ad.visitCount += 1
        ad.save()
    if ad.showInSite or ad.creator == request.user:
        return render(request, 'mainapp/show_ad_premium.html', {
            'ad': ad,
        })
    raise Http404


def show_cat(request, catUrl):
    """ Shows all Ads in Category """
    cat = get_object_or_404(AdCategory, url=catUrl)
    if not request.user.is_superuser:
        cat.visitCount += 1
        cat.save()
    return render(request, 'mainapp/show_cat.html',{
        'ads_list':  Advertisement.objects.filter(category=cat)[::-1],
        'cat_title': AdCategory.objects.get(url=catUrl),
        'cats_list': AdCategory.objects.all(),
    })


def show_all_ads(request):
    """ Shows all Ads with ContainInSlideShow checked """
    return render(request, 'mainapp/show_cat.html', {
        'ads_list': Advertisement.objects.all()[::-1],
        'all_ads' : 'همه طرح ها',
        'cats_list': AdCategory.objects.all()
    })
