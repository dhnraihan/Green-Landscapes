#!/usr/bin/env python
import os
import sys
import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'landscaping_project.settings')

# Add the project directory to the Python path
project_path = os.path.dirname(os.path.abspath(__file__))
if project_path not in sys.path:
    sys.path.append(project_path)

import django
django.setup()

# Import models after Django setup
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.images import ImageFile

# Import models after Django setup
from services.models import ServiceCategory, Service
from core.models import Testimonial, FAQ
from gallery.models import GalleryCategory, Portfolio, BeforeAfterImage
from bookings.models import BookingTimeSlot, BookingStatus

def populate_service_categories():
    categories = [
        {
            'name': 'Lawn Care',
            'description': 'Professional lawn maintenance services to keep your grass looking its best.',
        },
        {
            'name': 'Garden Design',
            'description': 'Creative garden design services to transform your outdoor spaces.',
        },
        {
            'name': 'Hardscaping',
            'description': 'Stone patios, walkways, retaining walls, and other hardscape features.',
        },
        {
            'name': 'Tree Services',
            'description': 'Tree planting, trimming, removal, and maintenance services.',
        },
        {
            'name': 'Irrigation',
            'description': 'Irrigation system design, installation, and maintenance.',
        }
    ]
    
    for category_data in categories:
        ServiceCategory.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'slug': category_data['name'].lower().replace(' ', '-'),
                'description': category_data['description']
            }
        )
    
    print(f"Added {len(categories)} service categories")

def populate_services():
    lawn_care = ServiceCategory.objects.get(name='Lawn Care')
    garden_design = ServiceCategory.objects.get(name='Garden Design')
    hardscaping = ServiceCategory.objects.get(name='Hardscaping')
    tree_services = ServiceCategory.objects.get(name='Tree Services')
    irrigation = ServiceCategory.objects.get(name='Irrigation')
    
    services = [
        {
            'name': 'Weekly Lawn Mowing',
            'category': lawn_care,
            'description': 'Our weekly lawn mowing service includes trimming edges, blowing away debris, and ensuring your lawn maintains a consistently well-groomed appearance.',
            'short_description': 'Regular professional lawn mowing for a perfectly manicured yard.',
            'price': 49.99,
            'price_suffix': '/week',
            'is_featured': True,
        },
        {
            'name': 'Lawn Fertilization',
            'category': lawn_care,
            'description': 'Our lawn fertilization program provides essential nutrients to promote thick, healthy grass growth throughout the growing season.',
            'short_description': 'Targeted fertilization to promote lush, green grass.',
            'price': 149.99,
            'price_suffix': '/application',
            'is_featured': False,
        },
        {
            'name': 'Garden Design Consultation',
            'category': garden_design,
            'description': 'Work with our experienced landscape designers to create a custom garden plan that matches your style, preferences, and property needs.',
            'short_description': 'Professional garden planning and design consultation.',
            'price': 199.99,
            'price_suffix': '',
            'is_featured': True,
        },
        {
            'name': 'Seasonal Planting',
            'category': garden_design,
            'description': 'Keep your garden looking vibrant year-round with our seasonal planting service. We select and install plants that thrive in each season.',
            'short_description': 'Seasonal flower and plant installation for year-round color.',
            'price': 299.99,
            'price_suffix': '/season',
            'is_featured': False,
        },
        {
            'name': 'Stone Patio Installation',
            'category': hardscaping,
            'description': 'Transform your outdoor living space with a custom stone patio. We offer various materials and designs to complement your home.',
            'short_description': 'Custom stone patio design and installation.',
            'price': 3500.00,
            'price_suffix': 'and up',
            'is_featured': True,
        },
        {
            'name': 'Retaining Wall Construction',
            'category': hardscaping,
            'description': 'Our professional team designs and builds sturdy, attractive retaining walls to manage slopes and create usable space in your landscape.',
            'short_description': 'Functional and attractive retaining walls for sloped properties.',
            'price': 2000.00,
            'price_suffix': 'and up',
            'is_featured': False,
        },
        {
            'name': 'Tree Pruning',
            'category': tree_services,
            'description': 'Professional tree pruning to maintain tree health, improve appearance, and promote strong growth.',
            'short_description': 'Expert tree trimming and shaping services.',
            'price': 200.00,
            'price_suffix': '/tree',
            'is_featured': True,
        },
        {
            'name': 'Tree Removal',
            'category': tree_services,
            'description': 'Safe and efficient tree removal services for damaged, diseased, or unwanted trees, including stump grinding.',
            'short_description': 'Complete tree removal and stump grinding services.',
            'price': 500.00,
            'price_suffix': 'and up',
            'is_featured': False,
        },
        {
            'name': 'Sprinkler System Installation',
            'category': irrigation,
            'description': 'Custom sprinkler system design and installation to ensure efficient watering for your lawn and garden.',
            'short_description': 'Professional irrigation system installation.',
            'price': 2500.00,
            'price_suffix': 'and up',
            'is_featured': True,
        },
        {
            'name': 'Drip Irrigation',
            'category': irrigation,
            'description': 'Water-efficient drip irrigation systems for gardens, flowerbeds, and container plants.',
            'short_description': 'Water-saving drip irrigation for gardens and planters.',
            'price': 1200.00,
            'price_suffix': 'and up',
            'is_featured': False,
        },
    ]
    
    for service_data in services:
        Service.objects.get_or_create(
            name=service_data['name'],
            defaults={
                'category': service_data['category'],
                'slug': service_data['name'].lower().replace(' ', '-'),
                'description': service_data['description'],
                'short_description': service_data['short_description'],
                'price': service_data['price'],
                'price_suffix': service_data['price_suffix'],
                'is_featured': service_data['is_featured'],
            }
        )
    
    print(f"Added {len(services)} services")

def populate_testimonials():
    testimonials = [
        {
            'name': 'John Smith',
            'position': 'Homeowner',
            'company': 'Residential Client',
            'testimonial': 'Green Landscapes transformed our backyard into a beautiful oasis. Their attention to detail and professionalism exceeded our expectations. We highly recommend their services!',
            'rating': 5,
            'is_featured': True,
        },
        {
            'name': 'Emily Johnson',
            'position': 'Property Manager',
            'company': 'Oakwood Apartments',
            'testimonial': 'We\'ve been using Green Landscapes for our commercial properties for over 3 years. Their team is reliable, thorough, and always responsive to our needs.',
            'rating': 5,
            'is_featured': True,
        },
        {
            'name': 'Michael Brown',
            'position': 'Homeowner',
            'company': 'Residential Client',
            'testimonial': 'The garden design service was excellent. They listened to what we wanted and created a beautiful, low-maintenance garden that we enjoy year-round.',
            'rating': 4,
            'is_featured': True,
        },
        {
            'name': 'Sarah Wilson',
            'position': 'Business Owner',
            'company': 'Wilson\'s Cafe',
            'testimonial': 'Our outdoor seating area looks amazing after Green Landscapes installed our patio and surrounding gardens. It has significantly increased our customer satisfaction!',
            'rating': 5,
            'is_featured': False,
        },
        {
            'name': 'David Thompson',
            'position': 'Homeowner',
            'company': 'Residential Client',
            'testimonial': 'Professional, punctual, and reasonably priced. They maintain our lawn weekly and it\'s never looked better.',
            'rating': 4,
            'is_featured': False,
        },
    ]
    
    for testimonial_data in testimonials:
        Testimonial.objects.get_or_create(
            name=testimonial_data['name'],
            testimonial=testimonial_data['testimonial'],
            defaults={
                'position': testimonial_data['position'],
                'company': testimonial_data['company'],
                'rating': testimonial_data['rating'],
                'is_featured': testimonial_data['is_featured'],
            }
        )
    
    print(f"Added {len(testimonials)} testimonials")

def populate_faqs():
    faqs = [
        {
            'question': 'How often should I water my lawn?',
            'answer': 'Most lawns need about 1-1.5 inches of water per week, either from rainfall or irrigation. It\'s better to water deeply and less frequently to encourage deep root growth. Water early in the morning to reduce evaporation.',
            'order': 1,
            'is_active': True,
        },
        {
            'question': 'When is the best time to fertilize my lawn?',
            'answer': 'The best time to fertilize cool-season grasses is in the fall and spring. For warm-season grasses, late spring through summer is ideal. We recommend a soil test to determine the specific needs of your lawn.',
            'order': 2,
            'is_active': True,
        },
        {
            'question': 'Do you offer maintenance contracts?',
            'answer': 'Yes, we offer various maintenance contracts tailored to your needs, from weekly lawn care to comprehensive landscape maintenance. Contact us for a customized maintenance plan.',
            'order': 3,
            'is_active': True,
        },
        {
            'question': 'How do I get an estimate for landscaping work?',
            'answer': 'You can request an estimate by calling our office, using the contact form on our website, or scheduling an appointment online. One of our landscape professionals will visit your property to discuss your needs and provide a detailed estimate.',
            'order': 4,
            'is_active': True,
        },
        {
            'question': 'What payment methods do you accept?',
            'answer': 'We accept cash, checks, and all major credit cards. For ongoing services, we offer automatic payment options for your convenience.',
            'order': 5,
            'is_active': True,
        },
        {
            'question': 'Do you provide emergency tree services?',
            'answer': 'Yes, we offer emergency tree services for fallen trees or dangerous situations. Contact our 24-hour emergency line for immediate assistance.',
            'order': 6,
            'is_active': True,
        },
        {
            'question': 'How do I care for newly planted trees and shrubs?',
            'answer': 'New plantings require regular watering during their establishment period (typically 1-2 years). We provide detailed care instructions for all new installations and offer maintenance services to ensure your plants thrive.',
            'order': 7,
            'is_active': True,
        },
    ]
    
    for faq_data in faqs:
        FAQ.objects.get_or_create(
            question=faq_data['question'],
            defaults={
                'answer': faq_data['answer'],
                'order': faq_data['order'],
                'is_active': faq_data['is_active'],
            }
        )
    
    print(f"Added {len(faqs)} FAQs")

def populate_gallery_categories():
    categories = [
        {
            'name': 'Residential Gardens',
            'description': 'Beautiful garden designs for residential properties.',
        },
        {
            'name': 'Commercial Landscaping',
            'description': 'Professional landscaping for business and commercial properties.',
        },
        {
            'name': 'Outdoor Living Spaces',
            'description': 'Patios, decks, and outdoor entertainment areas.',
        },
        {
            'name': 'Water Features',
            'description': 'Ponds, fountains, and other water elements.',
        },
        {
            'name': 'Seasonal Displays',
            'description': 'Seasonal plantings and holiday decorations.',
        },
    ]
    
    for category_data in categories:
        GalleryCategory.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'slug': category_data['name'].lower().replace(' ', '-'),
                'description': category_data['description']
            }
        )
    
    print(f"Added {len(categories)} gallery categories")

def populate_portfolio():
    residential = GalleryCategory.objects.get(name='Residential Gardens')
    commercial = GalleryCategory.objects.get(name='Commercial Landscaping')
    outdoor = GalleryCategory.objects.get(name='Outdoor Living Spaces')
    water = GalleryCategory.objects.get(name='Water Features')
    seasonal = GalleryCategory.objects.get(name='Seasonal Displays')
    
    portfolios = [
        {
            'title': 'Modern Backyard Retreat',
            'category': residential,
            'description': 'A complete backyard transformation featuring drought-tolerant plants, a stone patio, and ambient lighting.',
            'location': 'Oak Ridge Estates',
            'completion_date': datetime.date(2024, 3, 15),
            'is_featured': True,
        },
        {
            'title': 'Corporate Office Landscaping',
            'category': commercial,
            'description': 'Professional landscaping for a corporate headquarters, including seasonal plantings and irrigation system installation.',
            'location': 'Downtown Business District',
            'completion_date': datetime.date(2024, 2, 10),
            'is_featured': True,
        },
        {
            'title': 'Stone Patio with Outdoor Kitchen',
            'category': outdoor,
            'description': 'Custom stone patio featuring a built-in grill, outdoor kitchen, and dining area.',
            'location': 'Lakeside Heights',
            'completion_date': datetime.date(2024, 4, 5),
            'is_featured': True,
        },
        {
            'title': 'Natural Pond with Waterfall',
            'category': water,
            'description': 'Natural-looking pond with cascading waterfall and surrounding native plantings.',
            'location': 'Woodland Acres',
            'completion_date': datetime.date(2023, 8, 20),
            'is_featured': False,
        },
        {
            'title': 'Fall Color Display',
            'category': seasonal,
            'description': 'Vibrant fall planters and landscape featuring autumn colors and textures.',
            'location': 'Various Locations',
            'completion_date': datetime.date(2023, 9, 30),
            'is_featured': False,
        },
    ]
    
    for portfolio_data in portfolios:
        Portfolio.objects.get_or_create(
            title=portfolio_data['title'],
            defaults={
                'category': portfolio_data['category'],
                'description': portfolio_data['description'],
                'location': portfolio_data['location'],
                'completion_date': portfolio_data['completion_date'],
                'is_featured': portfolio_data['is_featured'],
            }
        )
    
    print(f"Added {len(portfolios)} portfolio items")

def populate_before_after_images():
    residential = GalleryCategory.objects.get(name='Residential Gardens')
    outdoor = GalleryCategory.objects.get(name='Outdoor Living Spaces')
    
    transformations = [
        {
            'title': 'Front Yard Makeover',
            'category': residential,
            'description': 'Complete transformation of a neglected front yard into a welcoming, low-maintenance landscape.',
            'location': 'Maple Street',
            'completion_date': datetime.date(2024, 1, 15),
            'is_featured': True,
        },
        {
            'title': 'Backyard Patio Transformation',
            'category': outdoor,
            'description': 'Conversion of an unused backyard space into a beautiful stone patio with seating and planting areas.',
            'location': 'River View Estates',
            'completion_date': datetime.date(2023, 7, 22),
            'is_featured': True,
        },
    ]
    
    for transformation_data in transformations:
        BeforeAfterImage.objects.get_or_create(
            title=transformation_data['title'],
            defaults={
                'category': transformation_data['category'],
                'description': transformation_data['description'],
                'location': transformation_data['location'],
                'completion_date': transformation_data['completion_date'],
                'is_featured': transformation_data['is_featured'],
            }
        )
    
    print(f"Added {len(transformations)} before/after transformations")

def populate_booking_time_slots():
    time_slots = [
        {'start_time': '08:00'},
        {'start_time': '09:00'},
        {'start_time': '10:00'},
        {'start_time': '11:00'},
        {'start_time': '12:00'},
        {'start_time': '13:00'},
        {'start_time': '14:00'},
        {'start_time': '15:00'},
        {'start_time': '16:00'},
        {'start_time': '17:00'},
    ]
    
    for slot_data in time_slots:
        BookingTimeSlot.objects.get_or_create(
            start_time=slot_data['start_time'],
            defaults={'is_available': True}
        )
    
    print(f"Added {len(time_slots)} booking time slots")

def populate_booking_statuses():
    statuses = [
        {
            'name': 'pending',
            'description': 'Booking request has been submitted but not yet confirmed.'
        },
        {
            'name': 'confirmed',
            'description': 'Booking has been confirmed and scheduled.'
        },
        {
            'name': 'in_progress',
            'description': 'Service is currently being performed.'
        },
        {
            'name': 'completed',
            'description': 'Service has been completed successfully.'
        },
        {
            'name': 'cancelled',
            'description': 'Booking has been cancelled.'
        },
    ]
    
    for status_data in statuses:
        BookingStatus.objects.get_or_create(
            name=status_data['name'],
            defaults={'description': status_data['description']}
        )
    
    print(f"Added {len(statuses)} booking statuses")

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        print("Created superuser: admin / adminpassword")
    else:
        print("Superuser 'admin' already exists")

if __name__ == '__main__':
    print("Starting Green Landscapes population script...")
    
    # Create superuser
    create_superuser()
    
    # Populate models
    populate_service_categories()
    populate_services()
    populate_testimonials()
    populate_faqs()
    populate_gallery_categories()
    populate_portfolio()
    populate_before_after_images()
    populate_booking_time_slots()
    populate_booking_statuses()
    
    print("Population completed!")
