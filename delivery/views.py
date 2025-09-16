from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Restaurant

# Create your views here.
def index(request):
    return render(request, 'index.html')

def open_signin(request):
    return render(request, 'signin.html')

def open_signup(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        try:
            Customer.objects.get(username=username)
            return HttpResponse("Duplicate username is not allowed")
        except Customer.DoesNotExist:
        # Check for duplicate username
            Customer.objects.create(
                username=username,
                password=password,
                email=email,
                mobile=mobile,
                address=address
            )
    return render(request, "signin.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            Customer.objects.get(username=username, password=password)
            if username == "admin":
                return render(request, "admin_home.html")
            else:
                return render(request, "customer_home.html")
            
        except Customer.DoesNotExist:
            return render(request, "fail.html")
        
def add_restaurant_page(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        Restaurant.objects.create(
            name=name,
            picture=picture,
            cuisine=cuisine,
            rating=rating
            )
        return render(request, 'add_restaurant.html')
    return render(request, "add_restaurant.html")
