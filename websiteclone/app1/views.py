from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html') 
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')
def orderonline(request):
    return render(request,'orderonline.html')
def profile(request):
    return render(request,'profile.html')
def restaruant(request):
    return render(request,'restaruant.html')
def dining(request):
    return render(request,'dining.html')
def events(request):
    return render(request,'events.html') 
def cart(request):
    return render(request,'cart.html')
def reservation(request):
    return render(request,'reservation.html')
