from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Listing

# Create your views here.


def index(request):
    listings = Listing.order_by('-listing_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
