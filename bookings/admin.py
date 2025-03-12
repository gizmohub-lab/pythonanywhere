from django.contrib import admin
from .models import Booking,homepagedesign

class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "number", "address", "program")  
    search_fields = ("name", "number", "program", "address") 
    list_filter = ("date",)  
    ordering = ("date",)  

    
    date_hierarchy = "date"

admin.site.site_header = "Janapriya Admin Panel"
admin.site.site_title = "Janapriya Auditorium"
admin.site.index_title = "All Bookings Available Here"

admin.site.register(Booking, BookingAdmin)
admin.site.register(homepagedesign)
