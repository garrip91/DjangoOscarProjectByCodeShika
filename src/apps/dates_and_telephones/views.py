from django.shortcuts import render

from .forms import PhoneAndDateForm

from django.http import HttpResponseRedirect


# Create your views here.
def save_phone_and_date(request):

    if request.method == 'GET':
        form = PhoneAndDateForm(request.GET)
        if form.is_valid():
            phone_and_date = form.save(commit=False)
            #phone_and_date.phone_number = '+79201561358'
            number = request.GET.get('phone_number')
            print(F"{number}")
            phone_and_date.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index.html', {'form': form})