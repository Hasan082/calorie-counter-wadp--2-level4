from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm, ProfileForm, CalorieForm
from .models import Profile, Calorie
from datetime import datetime
from django.db.models import Sum


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register Succesfull! Please login")
            return redirect("login")
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }

    return render(request, "pages/register.html", context)


def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            profile, created = Profile.objects.get_or_create(user=request.user)
            if created:
                return redirect('profile')
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    context = {"form": form, "login_form": True}
    return render(request, "pages/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if created:
        messages.warning(request, "Update your profile first")
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            profile, created = Profile.objects.get_or_create(user=request.user)
            return redirect("dashboard")
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'pages/profile.html', context)


@login_required
def calorie_entry_view(request):
    if request.method == "POST":
        form = CalorieForm(request.POST)
        if form.is_valid():
            profile_data = form.save(commit=False)
            profile_data.user = request.user
            profile_data.save()
            return redirect("dashboard")
    else:
        form = CalorieForm()
        
    context = {
        'form': form
    }
    
    return render(request, "pages/add-calorie.html", context)


@login_required
def dashboard_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    req_bmr = profile.bmr
    users_cal = Calorie.objects.filter(user=request.user)
    today_cal = users_cal.filter(date=datetime.now().date())
    
    calorie_data = today_cal.aggregate(total=Sum('calorie_consumed'))
    total_calories = calorie_data['total']
    conttext = {
        'req_bmr': req_bmr,
        'total_calories': total_calories,
        'users_cal': users_cal
    }
    return render(request, "pages/dashboard.html", conttext)
