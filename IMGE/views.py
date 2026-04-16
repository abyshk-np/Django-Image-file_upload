
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Added')
        else:
            messages.error(request, 'Error')
    else:
        form = ProfileForm()
    return render(request, 'uploadp.html', {'form': form})

def profile_view(request):
    profiles = Profile.objects.all()
    return render(request, 'profilev.html', {'profiles': profiles})

