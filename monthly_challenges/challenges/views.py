from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Play video games for 1 hour every day!",
    "may": "Go to the gym every day!",
    "june": "Cook a new recipe every day!",
    "july": "Read a new book every week!",
    "august": "Meditate for 10 minutes every day!",
    "september": "Write in your journal every day!",
    "october": "Take a photo every day!",
    "november": "Practice a new language for 15 minutes every day!",
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month < 1 or month > len(months):
        invalid_month = '<h1> This month is not supported! </h1>'
        return HttpResponseNotFound(invalid_month)

    redirect_month = months[month - 1]

    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        raise Http404()
