from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User, Subscriber
import logging
import datetime
logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')


def register_page(request):
    """ User Registration Function"""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password1']
        # check if phone already exist pass to login page
        if User.objects.filter(phone=phone).exists():
            return HttpResponseRedirect(reverse('authentication:login'))
        # if not create a user and pass to panel page
        user = User.objects.create_user(phone, password)
        user.name = name
        user.email = email
        user.phone = phone
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect(reverse('my:panel'))
    else:
        return render(request, 'mainapp/register.html')


def login_page(request):
    """ User Login Function"""

    if request.method == 'POST':
        username = request.POST['phone']
        password = request.POST['password']

        input_user = User.objects.filter(phone=username)

        if User.objects.filter(phone=username).exists():
            copy = input_user[0]
        else:
            return render(request, 'mainapp/login.html', {
                'incorrect': True,
            })

        now = datetime.datetime.now()

        if copy.attempts < 3:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return HttpResponseRedirect(reverse('my:panel'))
            else:
                # phone or password is incorrect
                logging.warning('suspicious attempts from user:{} - date:{}'.format(username, now))
                copy.attempts += 1
                copy.save()
                return render(request, 'mainapp/login.html', {
                    'incorrect': True,
                    })
        else:
            logging.warning('user locked because of failed attempts =>  user:{} - date:{}'.format(username, now))
            copy.is_active = False
            copy.save()

            return render(request, 'mainapp/login.html', {
                'locked': True
            })
    else:
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse('my:panel'))
        return render(request, 'mainapp/login.html')


def logout_page(request):
    """ User Logout Function"""
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def subscription(request):
    s = Subscriber.objects.create()
    s.email = request.POST['email']
    s.save()
    return HttpResponseRedirect(reverse('mainapp:index'))

