from django.shortcuts import render
from .forms import SignUpForm, ThingForm

#def home(request):
#    return render(request, 'home.html')

def sign_up(request):
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def home(request):
    form = ThingForm()
    return render(request, 'things_form.html', {'form': form})
