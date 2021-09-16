from django.db.models import Sum
from django.shortcuts import render

from events.models import Donate, Event


def index(request):
    event = Event.objects.all()
    amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
    context = {
        'events': event,
        'amount': amount
    }
    return render(request, 'index.html', context);


def about(request):
    return render(request, 'about.html');


def contact(request):
    return render(request, 'contact.html')


def causes(request):
    event = Event.objects.all()
    amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
    context = {
        'events': event,
        'amount': amount
    }
    return render(request, 'causes.html', context)

