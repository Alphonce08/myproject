from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib import admin




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
        phone = request.POST['phonenumber']
        amount = product.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "School fees"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("success")

    
    return render(request, 'payment.html')


def post(request, pk):
    return render(request, 'post.html')
