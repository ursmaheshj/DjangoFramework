from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app1_bank/index.html')

def about(request):
    return render(request,'app1_bank/about.html')

def getBalance(request):
    return render(request,'app1_bank/balance.html')