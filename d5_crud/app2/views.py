from django.shortcuts import render
from app2.forms import ModelUserForm
from app1.models import User

# Create your views here.
def ModelUserView(request):
    if request.method == 'POST':
        modeluserform = ModelUserForm(request.POST)
        # user = User.objects.get(id=2)               
        # modeluserform = ModelUserForm(request.POST,instance=user)  #To update existing record
        if modeluserform.is_valid():
            modeluserform.save()
    else:
        modeluserform = ModelUserForm()

    return render(request,'app2/modelform.html',{'modeluserform':modeluserform})