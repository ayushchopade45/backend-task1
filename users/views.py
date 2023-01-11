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
def morse(request):
    return render(request, 'users/morse.html')
def inverse(request):
    return render(request,'users/inverse.html')
def caesar(request):
    return render(request,'users/caesar.html')

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
def result2(request):
    val1 = request.GET["text1"]
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    cipher = ''
    for letter in val1:
        if letter != ' ':


            cipher =cipher+ MORSE_CODE_DICT[letter] + ' '
        else:

            cipher += ' '

    return render(request, 'users/result2.html', {"results": cipher})
def result3(request):
    val1 = request.GET["text1"]
    cipher=val1.swapcase()
    return render(request, 'users/result3.html', {"results": cipher})
def result4(request):
   plaintext = request.GET["text1"]
   n = int(request.GET["val1"])
   ans = ""

   for i in range(len(plaintext)):
       ch = plaintext[i]


       if ch == " ":
           ans += " "

       elif (ch.isupper()):
           ans += chr((ord(ch) + n - 65) % 26 + 65)


       else:
           ans += chr((ord(ch) + n - 97) % 26 + 97)
   return render(request, 'users/result4.html', {"results": ans})