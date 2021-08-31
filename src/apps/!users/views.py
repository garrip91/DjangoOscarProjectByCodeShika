from django.shortcuts import render

#from .models import User
from .forms import UserForm

# Create your views here.
def save_user(request):

    if request.method == 'GET':
        form = UserForm(request.GET)
        if form.is_valid():
            return render(request, 'index.html', {'form': form})
        else:
            return render(request, 'index.html', {'form': form})

    