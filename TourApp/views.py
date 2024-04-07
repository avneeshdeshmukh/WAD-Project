from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'index.html')


def loginUser(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username'].lower()
            password=form.cleaned_data['password']

            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid Username')
                return redirect('/login/')
            
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Wrong Password')
                return redirect('/login/')
            
            else:
                login(request, user)
                return redirect('/')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('/login/')

    return render(request, 'login.html')


def signupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username'].lower()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']

            if(password != confirmpassword):
                messages.error(request, 'Password match nahi hora aur isko tinder pe match chahiye🤡')
                return redirect('/signup/')

            user = User.objects.filter(username=username)

            if user.exists():
                messages.error(request, 'Username Already Taken')
                return redirect('/signup/')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Taken')
                return redirect('/signup/')
            else:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username)

                user.set_password(password)
                user.save()
                messages.success(request, 'Account Created Successfully!')

                return render(request, 'login.html', {'title': 'Login'})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('/signup/')
    return render(request, 'signup.html')


def restaurants(request):
    return render(request, 'restaurants.html')


def history(request):
    return render(request, 'history.html')


def transport(request):
    return render(request, 'transport.html')

def places(request):
    return render(request, 'places.html')

