from django.contrib import admin

# Register your models here.
from .models import profile, Addition
admin.site.register(profile)
admin.site.register(Addition)
