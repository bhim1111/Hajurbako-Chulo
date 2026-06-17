import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hajurbako_chulo_project.settings')
django.setup()

from restaurant.models import Category, MenuItem, GalleryItem, Testimonial

# Clear existing data
Category.objects.all().delete()
MenuItem.objects.all().delete()
GalleryItem.objects.all().delete()
Testimonial.objects.all().delete()

# Categories
main_course = Category.objects.create(name="Main Course", slug="main-course")
snacks = Category.objects.create(name="Snacks & Appetizers", slug="snacks")
desserts = Category.objects.create(name="Traditional Desserts", slug="desserts")

# Menu Items
MenuItem.objects.create(
    category=main_course,
    name="Thakali Dal Bhat Set",
    description="Authentic Thakali set with organic lentils, long-grain rice, seasonal vegetable curry, and spicy pickles.",
    price=850.00,
    image="menu_items/dal-bhat.jpg",
    is_featured=True
)

MenuItem.objects.create(
    category=snacks,
    name="Steamed Chicken Momo",
    description="Juicy chicken dumplings steamed to perfection, served with our signature sesame tomato chutney.",
    price=450.00,
    image="menu_items/momo.jpg",
    is_featured=True
)

MenuItem.objects.create(
    category=snacks,
    name="Mutton Sekuwa",
    description="Tender mutton marinated in Himalayan spices and charcoal-grilled for a smoky flavor.",
    price=750.00,
    image="menu_items/sekuwa.jpg",
    is_featured=True
)

MenuItem.objects.create(
    category=main_course,
    name="Newari Khaja Set",
    description="Traditional Newari platter with beaten rice, choila, bhatmas sandheko, and aila.",
    price=650.00
)

MenuItem.objects.create(
    category=desserts,
    name="Yomari",
    description="Steamed rice-flour dumpling filled with sweet molasses and sesame seeds.",
    price=250.00
)

# Testimonials
Testimonial.objects.create(
    name="Prashant Thapa",
    role="Regular Patron",
    content="The best Momo I've ever had! It tastes exactly like my grandmother's cooking. Truly authentic Nepali flavors.",
    rating=5
)

Testimonial.objects.create(
    name="Elena Rodriguez",
    role="Travel Blogger",
    content="An absolute hidden gem in Kathmandu. The Thakali Set is to die for. High-quality food and a lovely atmosphere.",
    rating=5
)

print("Check: Data populated successfully!")
