from django.shortcuts import render

# Create your views here.
def getBalance(request):
    return render(request,'app1_bank/index.html')