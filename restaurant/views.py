from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages

from .models import Category, MenuItem, Testimonial, GalleryItem, Reservation


class HomeView(TemplateView):
    template_name = "restaurant/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["featured_dishes"] = MenuItem.objects.filter(
            is_featured=True,
            is_available=True
        )[:6]

        context["categories"] = Category.objects.prefetch_related("items").all()
        context["testimonials"] = Testimonial.objects.all()
        context["gallery_items"] = GalleryItem.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        guests = request.POST.get("guests")
        message = request.POST.get("message")

        Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guests=guests,
            message=message,
        )

        messages.success(
            request,
            "Your table has been reserved successfully! We will contact you soon."
        )

        return redirect("home")