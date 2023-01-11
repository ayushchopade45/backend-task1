from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
import base64
# Create your views here.
def home(request):
    return render(request,'users/home.html')
def register(request):
    form=UserRegisterForm()
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            form.save()
            return redirect('login')
    return render(request,'users/register.html',{'form':form})
def options(request):
    return render(request, 'users/options.html')
def encode(request):
    return render(request, 'users/encode.html')
def decode(request):
    return render(request, 'users/decode.html')
def result(request):

    val1=request.GET["text1"]
    enc=val1.encode("ascii")
    asebytes=base64.b64encode(enc)
    enc1=asebytes.decode('ascii')
    return render(request,'users/result.html',{"results":enc1})
def result1(request):
    val1 = request.GET["text1"]
    enc = val1.encode("ascii")
    asebytes = base64.b64decode(enc)
    enc1 = asebytes.decode('ascii')
    return render(request, 'users/result1.html', {"results": enc1})
