from django.shortcuts import render,redirect
from .models import *
from instamojo_wrapper import Instamojo

API_KEY = "test_658225c502f26d265f88a678e3f"

AUTH_TOKEN = "test_c8ca64433a3086574c296e9d261"

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')


def donate(request):
    return render(request,'donation/donate.html')

def success(request):
    return render(request,'donation/success.html')

def pay(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        
        response = api.payment_request_create(
        amount=amount,
        purpose="donation",
        buyer_name=name,
        send_email=True,
        email=email,
        redirect_url="http://localhost:8000/success")
        
        return redirect(response['payment_request']['longurl'])
    
    else:
        
        return redirect('/')  