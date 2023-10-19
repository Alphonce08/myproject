from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View



def index(request):
    return render(request, 'index.html' )
def register(request):
    if request.method == 'POST':
    
      username = request.POST['username']
      email = request.POST['email']
      phonenumber = request.POST['phonenumber']
      password = request.POST['password']
      password2 = request.POST['password2']
    
      if password == password2:
          if User.objects.filter(email=email).exists():
              messages.info(request, 'Email already Exists')
              return redirect('register')
          elif User.objects.filter(username=username).exists():
              messages.info(request, 'Username already Exists')
              return redirect('register')
          else:
              user =  User.objects.create_user(username=username, password=password)
              user.save();
              return redirect('login')
      else:
          messages.info(request, 'password is not the same')            
          return redirect('register')
    else:
      return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
      return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def payment(request):
    if request.method == "POST":
        phonenumber = request.POST.get('phonenumber')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'WANYAMA'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phonenumber, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)
    return render(request, 'payment.html')
