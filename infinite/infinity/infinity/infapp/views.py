from django.shortcuts import render

def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog_grid_2.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def gallery(request):
    return render(request, "gallery_filter.html")


def industries(request):
    return render(request, "industries.html")


def industries_details(request):
    return render(request, "industries_details.html")


def portfolio(request):
    return render(request, "portfolio.html")


def products(request):
    return render(request, "product.html")


def product_details(request):
    return render(request, "product_details.html")


def projects(request):
    return render(request, "projects.html")


def project_details(request):
    return render(request, "project_details.html")


def services(request):
    return render(request, "services.html")


def services_carousel(request):
    return render(request, "services_carousel_3.html")


def services_alt(request):
    return render(request, "services_2.html")


def service_details(request):
    return render(request, "service_details.html")


def team(request):
    return render(request, "team.html")


def team_details(request):
    return render(request, "team_details.html")


def technology(request):
    return render(request, "technology.html")


def technology_details(request):
    return render(request, "technology_details.html")


def testimonials(request):
    return render(request, "testimonials.html")


def error_404(request):
    return render(request, "404.html")