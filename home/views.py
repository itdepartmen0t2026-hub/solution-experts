from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    pro=Product.objects.values('title','slug')
    product=Product.objects.filter(is_active=True)
    return render(request,'index.html',{'pro':pro,'product':product})

def about(request):
    pro=Product.objects.values('title','slug')
    return render(request,'about.html',{'pro':pro})

def services(request):
    pro=Product.objects.values('title','slug')
    return render(request,'services.html',{'pro':pro})

def industries(request):
    pro=Product.objects.values('title','slug')
    return render(request,'industries.html',{'pro':pro})

def quality(request):
    pro=Product.objects.values('title','slug')
    return render(request,'quality.html',{'pro':pro})

def career(request):
    pro=Product.objects.values('title','slug')
    return render(request,'career.html',{'pro':pro})

def contect(request):

    pro = Product.objects.values('title', 'slug', 'id')

    if request.method == 'POST':

        name = request.POST.get('Name', '').strip()
        phone = request.POST.get('Phone', '').strip()
        email = request.POST.get('Email', '').strip()
        company = request.POST.get('Company', '').strip()
        product = request.POST.get('Product', '').strip()
        requirement = request.POST.get('Requirement', '').strip()

        # Validation
        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'contact.html', {'pro': pro})

        if len(name) < 2:
            messages.error(
                request,
                'Name must be at least 2 characters.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if not phone:
            messages.error(
                request,
                'Phone number is required.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if not phone.isdigit():
            messages.error(
                request,
                'Phone number must contain only digits.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if len(phone) != 10:
            messages.error(
                request,
                'Phone number must be 10 digits.'
            )
            return render(request, 'contact.html', {'pro': pro})

        if email:
            try:
                validate_email(email)
            except ValidationError:
                messages.error(
                    request,
                    'Please enter a valid email address.'
                )
                return render(
                    request,
                    'contact.html',
                    {'pro': pro}
                )

        if not product:
            messages.error(
                request,
                'Please select a product.'
            )
            return render(
                request,
                'contact.html',
                {'pro': pro}
            )

        # Save enquiry
        Enquiry.objects.create(
            name=name,
            phone=phone,
            email=email or None,
            company=company or None,
            product=product,
            requirement=requirement or None
        )

        # Send email
        subject = f'New Enquiry - {name}'

        message = f"""
New Enquiry Received

Name: {name}
Phone: {phone}
Email: {email}
Company: {company}
Product / Service: {product}

Requirement:
{requirement}
"""

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['kpsales32@gmail.com'],
            fail_silently=False,
        )

        messages.success(
            request,
            'Your enquiry has been submitted successfully.'
        )

        return redirect('contact')

    return render(
        request,
        'contact.html',
        {'pro': pro}
    )

def allproduct(request):
    pro=Product.objects.values('title','slug')
    product=Product.objects.filter(is_active=True)
    return render(request,'products.html',{'product':product,'pro':pro})

def product(request,title):
    pro=Product.objects.values('title','slug')
    product=Product.objects.get(is_active=True,slug=title)
    return render(request,'dowel-bar-cap.html',{'product':product,'pro':pro})