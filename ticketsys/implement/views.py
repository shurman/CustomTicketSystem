from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse, resolve
from django.utils import timezone
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
    ticket_list = Ticket.objects.all()
    if request.user.groups.filter(name='QA').exists():
        is_qa = True
    else:
        is_qa = False
    if request.user.groups.filter(name='PM').exists():
        is_pm = True
    else:
        is_pm = False

    return render(request, 'user_main.html', locals())

@login_required()
def ticket_new(request):
    is_rd = False
    is_qa = False
    is_pm = False
    if request.user.groups.filter(name='RD').exists():
        is_rd = True
    if request.user.groups.filter(name='QA').exists():
        is_qa = True
    if request.user.groups.filter(name='PM').exists():
        is_pm = True

    if request.method == 'POST':
        if is_qa or is_pm:
            newticket = Ticket()
            newticket.title = request.POST.get('title','')
            newticket.t_type = '0' if is_qa else '1'
            newticket.status = '0'
            newticket.severity = request.POST.get('severity','')
            newticket.description = request.POST.get('description','')
            newticket.creator = request.user
            newticket.create_date = timezone.now()

            if newticket.title != '':
                newticket.save()

        return HttpResponseRedirect(reverse('user_main'))
    return render(request, 'ticket_main.html', locals())

@login_required()
def ticket_show(request, tid):
    ticket = Ticket.objects.filter(id=tid).first()
    is_rd = False
    is_qa = False
    is_pm = False
    if request.user.groups.filter(name='RD').exists():
        is_rd = True
    if request.user.groups.filter(name='QA').exists():
        is_qa = True
    if request.user.groups.filter(name='PM').exists():
        is_pm = True

    if request.method == 'POST':
        if is_qa:
            ticket.title = request.POST.get('title','')
            ticket.status = request.POST.get('status','')
            ticket.severity = request.POST.get('severity','')
            ticket.description = request.POST.get('description','')
            ticket.save()
        elif is_rd:
            _status = request.POST.get('status','')
            if _status == '0' or _status == '1':
                ticket.status = request.POST.get('status','')
                ticket.save()
        return HttpResponseRedirect(reverse('user_main'))

    if ticket is None:
        return HttpResponseRedirect(reverse('user_main'))

    return render(request, 'ticket_main.html', locals())
