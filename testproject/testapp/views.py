from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'testapp/home.html')

def logout(request):
    return render(request,'testapp/logout.html')
def signup(request):
    return render(request,'testapp/signup.html')

