from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from ads.models import AdCategory, Advertisement, State
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import datetime

# Registered User Options
@login_required()
def panel_page(request):
    """ User panel Function"""
    if request.user.isInvestor:
        return redirect(reverse('my:all_ads'))
    return render(request, 'mainapp/panel.html', {
        'user': request.user,
        'ads_list': Advertisement.objects.filter(creator=request.user)[::-1]
    })


@login_required()
def create_ad(request):
    if request.method == 'POST':
        # Todo: make it flexible to hande edit ads !
        # check if title in unique
        adID = None
        if 'id' in request.POST:
            adID = request.POST['id']
        # to see the request is edit or create a new
        ad, is_new = Advertisement.objects.get_or_create(id=adID)
        if is_new:
            if Advertisement.objects.filter(title=request.POST['title']):
                return render(request, 'mainapp/create-ad.html', {
                    'ad_exist': request.POST['title'],
                    'cat_list': AdCategory.objects.all(),
                    'user': request.user,
                    'states_list': State.objects.all()
                })
        ad.title = request.POST['title']
        ad.creator = request.user
        ad.owner = request.POST['owner']
        ad.phone = request.POST['phone']
        ad.fund = request.POST['fund']
        ad.location = State.objects.get(title=request.POST['location'])
        ad.category = AdCategory.objects.get(url=request.POST['category'])
        ad.summary = request.POST['summary']
        showInSite = 'showInSite' in request.POST
        ad.showInSite = showInSite
        isLegal = 'isLegal' in request.POST
        ad.isLegal = isLegal
        # TODO: should be optional
        ad.save()
        return redirect(reverse('my:investment', kwargs={
            'adID': ad.id,
        }))
    else:
        return render(request, 'mainapp/create-ad.html', {
            'cat_list': AdCategory.objects.all(),
            'user': request.user,
            'states_list': State.objects.all(),
        })


@login_required()
def edit_ad(request, adID):
    """ Edits a certain ad with unique ID """
    return render(request, 'mainapp/edit_ad.html', {
            'cat_list': AdCategory.objects.all(),
            'user': request.user,
            'ad': get_object_or_404(Advertisement, id=adID),
            'states_list': State.objects.all(),
    })


@login_required()
def show_all_ads(request):
    """ Shows all Ads belong to User """
    if request.user.isInvestor:
        investor = request.user.investor_set.all()
        ads = Advertisement.objects.filter(investor=investor)[::-1]
    else:
        ads = Advertisement.objects.filter(creator=request.user)[::-1]
    return render(request, 'mainapp/my_ads.html', {
        'ads_list': ads
    })


@login_required()
def delete_ad(request, adID):
    """ Delete a certain ad """
    ad = get_object_or_404(Advertisement, id=adID)
    ad.delete()
    return redirect(reverse('my:panel'))


@login_required()
def change_pass(request):
    """ change password in panel """
    if request.method == 'POST' and 'password1' in request.POST:
        if request.POST['password1'] == request.POST['password2']:
            request.user.set_password(request.POST['password1'])
            request.user.save()
            login(request, request.user)
            return redirect(reverse('my:panel'))
        else:
            return render(request, 'mainapp/change_pass.html', {
                'notmatch': True,
            })

    return render(request, 'mainapp/change_pass.html')


@login_required()
def investment(request, adID):
    """ invest a certain ad """
    ad = get_object_or_404(Advertisement, id=adID)
    if request.method == 'POST' and not ad.isInterviewOK:
        if not ad.review:
            ad.expected_gain = request.POST['expected_gain']

            ad.expected_time = request.POST['expected_time']

            if 'images' in request.FILES:
                ad.images = request.FILES['images']
            if 'proposal' in request.FILES:
                ad.proposal = request.FILES['proposal']

            ad.executiveSummary = request.POST['exe_outline']

            ad.fundUsage = request.POST['usage']

            ad.presentIncome = request.POST['present_income']

            ad.resume = request.POST['resume']

            ad.investorShare = request.POST['investor_share']

            ad.estimatedCosts = request.POST['costs']

            ad.credits = request.POST['credits']

            ad.revenueModel = request.POST['revenue_model']

            ad.damage = request.POST['damage']

            ad.benefitShare = request.POST['benefit_share']

            ad.marketingPlan = request.POST['marketing_plan']

            ad.marketSize = request.POST['market_size']

            ad.rateOfReturn = request.POST['rate_of_return']

            ad.compet = request.POST['compet']

            ad.presentCustomers = request.POST['present_customers']

            ad.save()

            return redirect(reverse('my:pay:pay_for_review', kwargs={
                'adID': adID,
            }))
        ad.fundingStep = request.POST['step']
        ad.requestDate = datetime.date.today()
        ad.save()
        return redirect(reverse('my:panel'))
    if ad.isInterviewOK:
        ad.fundingStep = '2'
        ad.save()
    if ad.isInterviewOK:
        ad.fundingStep = '2'
        ad.save()
    return render(request, 'mainapp/investment.html', {
        'ad': ad,
    })


