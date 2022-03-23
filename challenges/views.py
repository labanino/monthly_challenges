from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    'january': 'Go to the gym!',
    'february': 'Take Yoga classes',
    'march': 'Learn React JS',
    'april': 'Practice React every day for 1 hour',
    'may': 'Learn how to cook lassagna',
    'june': 'Go on vacation to Europe',
    'july': 'Move to a new house',
    'august': 'Learn Day Trading',
    'september': 'Swimg 5 miles every day',
    'october': 'Pay attengion to my diet',
    'november': 'Go to visit my mom',
    'december': 'Prepare Christmas party'
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month]
    return HttpResponseRedirect('/challanges/' + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')
