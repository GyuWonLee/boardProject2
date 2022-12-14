from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.urls import reverse
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password=raw_password)
            login(request, user)
            return redirect(reverse('noticeboard:index'))

    else:
        form = UserForm()

    return render(request, 'registration/signup.html', {'form': form})



