''' -*- coding: utf-8 -*- MYBOOK VIEWS '''


from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Quote, User


# Create your views here.
def index(request):

    if not checkAuth(request):
        return redirect('/')

    user = User.objects.get(id=request.session.get('id'))
    quote = Quote.objects.all().order_by('-created_at')[:5]
    context = {
        'user': user,
        'quotes': quote,
    }
    return render(request, 'my_book/index.html', context)


def addQuote(request):
    # print 'at addquote in views'
    if not checkAuth(request):
        return redirect('/')

    if request.POST:
        results = Quote.objects.addQuote(request.POST)
        if results:
            messages.info(request, 'Quote Added')
        else:
            for error in results:
                messages.error(request, error)
            return redirect('mybook:addQuote')
        return redirect('mybook:index')

    user = User.objects.get(id=request.session.get('id'))
    context = {
        'user': user,
    }
    return render(request, 'my_book/addQuote.html', context)


def addFavorite(request):
    print 'at favorites in views'
    if request.POST:
        results = Quote.objects.addFavorite(request.POST, request.session['id'])
        if results:
            messages.info(request, 'Favorited!')
        else:
            for error in results:
                messages.error(request, error)
        return redirect('mybook:index')


def checkAuth(request):  # Force non-authorized user back to login/registration page
    try:
        if not request.session.get('id'):
            messages.error(request, 'Sorry, you\'re not logged in!')
            return False
        return True
    except:
        messages.error(request, 'Sorry, you\'re not logged in')
        return False
