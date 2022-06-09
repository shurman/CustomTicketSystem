from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse, resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_main'))

    if request.method == 'POST':
        form = LoginForm(request.POST or None)

        if form.is_valid():
            print(form.__dict__)
            auth.login(request, form.user)
            return HttpResponseRedirect(reverse('user_main'))
    else:
        form = LoginForm()
    return render(request, 'user_login.html', locals())

def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required()
def user_main(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_login'))

    ticket_list = Ticket.objects.all()
    return render(request, 'user_main.html', {'ticket_list':ticket_list})


@login_required()
def ticket_show(request, tid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_login'))
    ticket = Ticket.objects.filter(id=tid).first()

    if ticket is None:
        return HttpResponseRedirect(reverse('user_main'))

    return render(request, 'ticket_main.html', {'ticket':ticket})
