from django.urls import path

from infapp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('industries/', views.industries, name='industries'),
    path('industries/details/', views.industries_details, name='industries-details'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('products/', views.products, name='products'),
    path('products/details/', views.product_details, name='product-details'),
    path('projects/', views.projects, name='projects'),
    path('projects/details/', views.project_details, name='project-details'),
    path('services/', views.services, name='services'),
    path('services/carousel/', views.services_carousel, name='services-carousel'),
    path('services/alt/', views.services_alt, name='services-alt'),
    path('services/details/', views.service_details, name='service-details'),
    path('team/', views.team, name='team'),
    path('team/details/', views.team_details, name='team-details'),
    path('technology/', views.technology, name='technology'),
    path('technology/details/', views.technology_details, name='technology-details'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('404/', views.error_404, name='404'),
]
