from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ExamFormForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def fill_form(request):
    form = ExamFormForm()
    if request.method == 'POST':
        form = ExamFormForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    return render(request, 'form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')