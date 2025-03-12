from django.urls import path
from . import views

urlpatterns = [
     path('', views.calendar_view, name='calendar'),  # This will load index.html
    path('get_booked_dates/', views.get_booked_dates, name='get_booked_dates'),
    path('book_date/',views.book_date, name='book_date'),
    path ('home/',views.homepage,name='home')
]