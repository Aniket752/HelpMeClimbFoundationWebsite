from django.contrib import admin
from .models import donation,volunteer,massage,donationMade,recipt
# Register your models here.
admin.site.register(donation)
admin.site.register(volunteer)
admin.site.register(massage)
admin.site.register(donationMade)
admin.site.register(recipt)
