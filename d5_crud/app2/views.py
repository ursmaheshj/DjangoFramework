from django.shortcuts import render
from app2.forms import ModelUserForm

# Create your views here.
def ModelUserView(request):
    if request.method == 'POST':
        modeluserform = ModelUserForm(request.POST)
    else:
        modeluserform = ModelUserForm()

    return render(request,'app2/modelform.html',{'modeluserform':modeluserform})