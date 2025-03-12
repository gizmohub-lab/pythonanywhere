from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Booking,homepagedesign
import json


def homepage (req):
    lsts = homepagedesign.objects.all()
    return render (req,'home.html',{'lsts':lsts})

def calendar_view(request):
    return render(request, 'index.html')

def get_booked_dates(request):
    """Return booked dates as JSON"""
    booked_dates = list(Booking.objects.values_list('date', flat=True))
    return JsonResponse({"booked_dates": booked_dates})

@csrf_exempt
def book_date(request):
    """Save a new booking from the frontend"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            Booking.objects.create(
                name=data["name"],
                number=data["number"],
                date=data["date"],  # Only date, no time
                address=data["address"],
                program=data["program"]
            )
            return JsonResponse({"success": True})
        except:
            return JsonResponse({"success": False, "error": "Date already booked!"})
