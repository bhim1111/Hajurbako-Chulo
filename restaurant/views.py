from django.shortcuts import render, redirect
from .models import Category, MenuItem, Testimonial, GalleryItem, Reservation
from django.contrib import messages

def home(request):
    featured_dishes = MenuItem.objects.filter(is_featured=True, is_available=True)[:6]
    categories = Category.objects.prefetch_related('items').all()
    testimonials = Testimonial.objects.all()
    gallery_items = GalleryItem.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        
        Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guests=guests,
            message=message
        )
        messages.success(request, 'Your table has been reserved successfully! We will contact you soon.')
        return redirect('home')

    context = {
        'featured_dishes': featured_dishes,
        'categories': categories,
        'testimonials': testimonials,
        'gallery_items': gallery_items,
    }
    return render(request, 'restaurant/home.html', context)
