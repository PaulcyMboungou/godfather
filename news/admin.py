from django.contrib import admin

from .models import Location, User, Article

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Location)
