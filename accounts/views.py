from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Song, Artist, Concert
from .forms import LoginForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    username = request.user.username
    return render(request, 'registration/dashboard.html', {'username': username})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'registration/song_list.html', {'songs': songs})

def art(request):
    art = Artist.objects.all()
    return render(request, 'registration/art.html', {'art': art})

def concert(request):
    concerts = Concert.objects.all()
    return render(request, 'registration/concert.html', {'concerts': concerts})
