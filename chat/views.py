from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from templates.form import createuserform

from templates.form import createuserform

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = createuserform()

    return render(request, 'register.html', {'form':form})