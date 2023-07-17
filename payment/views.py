from django.contrib import messages
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User

def changep(request):
    return render(request, 'payment/passwordchange.html')


def changepassword(request):
    username = request.POST.get('name')
    oldpassword = request.POST.get('oldpassword')
    newpassword = request.POST.get('newpassword')
    try:
        user = User.objects.get(name=username)
    except:
        return HttpResponse("User doesn't exist")
    if request.method == 'POST' and oldpassword == user.password1:
        user.password1 = newpassword
        user.save()
        return HttpResponse("password changed sucessfully")
    else:
        return HttpResponse("Old password don't match")


def pay(request):
    return render(request, 'payment/khaltirequest.html')


def khalti_payment_verify(request):
    token = request.GET.get('token')
    amount = request.GET.get('amount')
    bill_id = request.GET.get('bill_id')
    payload = {
        "token":token,
        "amount":amount,
    }
    headers = {
        "Authorization": "Key {}".format("test_secret_key_82b6e7fde53c4a8890f5781459ed8560")
    }
    amount = int(amount)
    try:
        response = requests.post("https://khalti.com/api/v2/payment/verify/",payload,headers=headers)
        if response.status_code == 200 :
   
 
            return JsonResponse({"Success": "Payment Success"})
            

        else:
            messages.success(request, "Bad Resposne could not verify payment")
            return JsonResponse({"Error": "Bad Resposne could not verify payment"})

    except Exception as e:
        return JsonResponse({"Error": e})
    
def message(request):
    messages.success(request, "Payment Success")
    return render(request, "payment/message.html")