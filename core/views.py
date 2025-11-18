from django.shortcuts import render, redirect
from .models import Slide
from .forms import ContactForm

def home(request):
    slides = Slide.objects.all()
    form = ContactForm()
    return render(request, 'core/home.html', {'slides': slides, 'form': form})

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('home')

from django.shortcuts import render

def home(request):
    # static image filenames — template will use {% static %}
    slides = [
        'images/slide1.jpg',
        'images/slide2.jpg',
        'images/slide3.jpg',
    ]
    # hero image path (static)
    hero_image = 'images/hero.jpg'
    return render(request, 'core/home.html', {'slides': slides, 'hero_image': hero_image})
from django.shortcuts import render
from django.templatetags.static import static   # ← VERY IMPORTANT

def home(request):
    slides = [
        'images/slide1.jpg',
        'images/slide2.jpg',
        'images/slide3.jpg',
    ]

    # Hero image full URL using static()
    hero_image = static('images/hero.jpg')

    return render(request, 'core/home.html', {
        'slides': slides,
        'hero_image': hero_image
    })
from django.shortcuts import render
from django.templatetags.static import static

def home(request):
    slides = [
        'images/slide1.jpg',
        'images/slide2.jpg',
        'images/slide3.jpg'
    ]
    hero_image = static('images/hero.jpg')
    return render(request, 'core/home.html', {
        'slides': slides,
        'hero_image': hero_image
    })
from django.shortcuts import render

def contact(request):
    return render(request, 'core/contact.html')

def contact_submit(request):
    return render(request, 'core/contact_success.html')
def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def projects(request):
    return render(request, 'core/projects.html')
def team(request):
    return render(request, 'core/team.html')

def pricing(request):
    return render(request, 'core/pricing.html')
