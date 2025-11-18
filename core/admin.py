from django.contrib import admin
from .models import Slide, ContactMessage

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

from django.shortcuts import render
from .models import Slide

def home(request):
    slides = Slide.objects.all()
    # optionally use first slide as hero background
    hero_image = slides.first().image.url if slides.exists() else None
    return render(request, 'core/home.html', {'slides': slides, 'hero_image': hero_image})
