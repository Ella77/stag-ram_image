from django.contrib import admin
from .models import Photo

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    # list_display = ['content','image','filtered_image']filtered_image
    admin.site.register(Photo)