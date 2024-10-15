from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Profile,Tasks,Accounts


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confPassword = request.POST['re-password']
        if password != confPassword :
            return redirect ("/signup")
        newUser = User.objects.create_user(username , email , password)
        newUser.save()
        messages.success(request , "new account created!")
        return redirect('/')
    
    return render(request , 'register.html')

def handlelogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request , 'login.html')

def handlelogout(request):
    logout(request)
    return redirect('/login')

@login_required
def home(request):
    tasks = Tasks.objects.filter(user=request.user).count()
    pendingTask = Tasks.objects.filter(user=request.user , status='pending').count()
    submittedTask = Tasks.objects.filter(user=request.user, status='submitted').count()
    profile = Profile.objects.filter(user=request.user).first()
    profile = Profile.objects.filter(user=request.user).first()
    percentage = (pendingTask/tasks)*100
    try:
        account = Accounts.objects.filter(user = request.user).first()
        salary = account.salary()
    except:
        account = Accounts.objects.filter(user = request.user).first()
        salary = None
    param = {
        'account' : account ,
        'salary' : salary,
        'profile' : profile,
        'pendingTask':pendingTask,
        'submittedTask':submittedTask,
        'tasks' : tasks,
        'per' : percentage,
    }
    return render(request , 'home.html' , param)
@login_required
def payments(request):
    profile = Profile.objects.filter(user=request.user).first()
    try:
        account = Accounts.objects.filter(user = request.user).first()
        salary = account.salary()
    except:
        account = Accounts.objects.filter(user = request.user).first()
        salary = None
    param = {
        'account' : account ,
        'salary' : salary,
        'profile' : profile
    }
    return render(request , 'payments.html' , param)

@login_required
def tasks(request):
    pendingTask = Tasks.objects.filter(user=request.user , status='pending')
    submittedTask = Tasks.objects.filter(user=request.user, status='submitted')
    profile = Profile.objects.filter(user=request.user).first()
    attr = {
        'pendingTask':pendingTask,
        'submittedTask':submittedTask,
        'profile':profile,
    }
    return render(request , 'tasks.html' , attr)

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    try:
        account = Accounts.objects.filter(user = request.user).first()
        salary = account.salary()
    except:
        account = Accounts.objects.filter(user = request.user).first()
        salary = None
    param = {
        'account' : account ,
        'salary' : salary,
        'profile' : profile
    }
    
    return render(request , 'profile.html',param)
