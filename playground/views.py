from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.




def say_hello(request):
    # Pull data from db
    # Tansform
    # Send emails
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            return render(request, 'index.html', {'name' : name,
                                                  'email' : email,
                                                  'password1': password1,
                                                  'password2': password2})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "hello.html", {"form": form})

def another_page_view(request):
    return render(request, 'index.html')
