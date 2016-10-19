from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseRedirect
from .models import Secrets
from ..login.models import User

def secret(request):
    if 'id' not in request.session:
        messages.error(request, 'Please log in to continue.')
        return redirect(reverse('login:index'))
    context={
        'data':User.objects.filter(id=request.session['id'])[0],
        'secrets':Secrets.objects.annotate(tot_likes=Count('likes')).order_by('-created_at')[:5],
    }
    return render(request, 'secret/recent.html', context)

def create(request):
    if request.method=='POST':
        Secrets.objects.addSecret(request.POST)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect(reverse('secret:index'))

def delete(request, s_id):
    Secrets.objects.deleteSecret(s_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def like(request, s_id):
    if 'id' not in request.session:
        message.error(request, 'Please log in to continue.')
        return redirect(reverse('login:index'))
    Secrets.objects.addLike(request.session['id'],s_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def popular(request):
    if 'id' not in request.session:
        message.error(request, 'Please log in to continue ')
        return redirect(reverse('login:index'))
    context={
        'data':User.objects.filter(id=request.session['id'])[0],
        'secrets':Secrets.objects.annotate(tot_likes=Count('likes')).order_by('-tot_likes'),
    }
    return render(request, 'secret/popular.html', context)
