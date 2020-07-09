from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .models import MyUser
from Pharmacy.models import Profile, Pharmacy, Drug

# Create your views here.
def index(request):
    logout(request)
    return render(request, 'accounts/index.html')

def consumer_registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is None:
            currentUser = MyUser.objects.create_user(email=email, password=password)

            # create profile
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            contact = request.POST['contact']
            city = request.POST['city']
            region = request.POST['region']
            country = request.POST['country']
            Profile.objects.create(
                user = currentUser,
                firstname = firstname,
                lastname = lastname,
                contact = contact,
                city = city,
                region = region,
                country = country
            )

            # login user
            login(request, currentUser)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.add_message(request, messages.ERROR, 'Error creating account. Please try again')
            return HttpResponseRedirect(reverse('accounts:consumer_registration'))
    return render(request, 'accounts/consumer_registration.html')

def pharmacy_registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is None:
            currentUser = MyUser.objects.create_user(email=email, password=password)
            # crete profile
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            Profile.objects.create(user=currentUser, firstname=firstname, lastname=lastname, is_pharmacist=True)
            login(request, currentUser)
            return HttpResponseRedirect(reverse('accounts:pharmacy_setup'))
        else:
            messages.add_message(request, messages.ERROR, 'Error creating account. Please try again')
            return HttpResponseRedirect(reverse('accounts:pharmacy_registration'))
    return render(request, 'accounts/pharmacy_registration.html')

def pharmacy_setup(request):
    if request.method == 'POST':
        admin = request.user
        name = request.POST['name']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        contact = request.POST['contact']
        website = request.POST['website']
        Pharmacy.objects.create(
            admin = admin,
            name = name,
            loc_long = longitude,
            loc_lat = latitude,
            contact = contact,
            website = website,
        )
        login(request, admin)
        return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'accounts/pharmacy_setup.html')

def authLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.add_message(request, messages.ERROR, 'Error logging in. Please try again')
            return HttpResponseRedirect(reverse('accounts:login'))
    return render(request, 'accounts/login.html')

def dashboard(request):
    pharma_drugs = []
    if request.user.user.is_pharmacist:
        pharmacy = Pharmacy.objects.get(admin=request.user)
        pharma_drugs = pharmacy.drug_set.all()
    return render(request, 'accounts/dashboard.html', {
        'drugs': pharma_drugs,
    })

def add_drug(request):
    if request.method == 'POST':
        name = request.POST['name']
        qty = request.POST['quantity']
        drug = Drug(name=name, quantity=qty)
        drug.save()
        pharm = Pharmacy.objects.get(admin=request.user)
        drug.pharmacy.add(pharm)
        return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'accounts/add_drug.html')

def edit_drug(request, drug_id):
    drug = Drug.objects.get(id=drug_id)
    if request.method == 'POST':
        new_name = request.POST['name']
        new_qty = request.POST['quantity']
        drug.name = new_name
        drug.quantity = new_qty
        drug.save()
        return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'accounts/edit_drug.html', {'drug': drug})

def delete_drug(request, drug_id):
    drug = Drug.objects.get(id=drug_id)
    drug.delete()
    drug.save()
    return HttpResponseRedirect(reverse('dashboard'))
