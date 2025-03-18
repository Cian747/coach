from django.contrib import admin
from .models import Sport,Location,Profile,Comment,Wishlist,SportAdvert
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(Sport)
admin.site.register(SportAdvert)
admin.site.register(Wishlist)