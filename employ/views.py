from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import *


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confPassword = request.POST['re-password']
        code = request.POST['code']
        addemp = AddEmployee.objects.filter(code=code).first()
        if addemp is None:
            return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Denied</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f8d7da;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .error-container {
            background: #721c24;
            color: #f8d7da;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            max-width: 500px;
        }
        .error-icon {
            font-size: 50px;
            color: #f8d7da;
        }
        .error-message {
            font-size: 18px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-icon">&#9888;</div>
        <h2>Access Denied</h2>
        <p class="error-message">We detected that you are not an employee of our company or not recommended by our recruiter.<br>
        Please contact our HR department for more information.</p>
    </div>
</body>
</html>''')
        if password != confPassword :
            return redirect ("/signup")
        newUser = User.objects.create_user(username , email , password)
        newUser.save()
        account = Accounts(user=newUser, basic=0, bonus=0, reward=0)
        profile = Profile(user=newUser, employPost=addemp.post, employDate='2021-01-01')
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
    try:
        percentage = (pendingTask/tasks)*100
        account = Accounts.objects.filter(user = request.user).first()
        salary = account.salary()
    except:
        percentage = 0
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
    email = request.user.email
    username = request.user.username
    try:
        account = Accounts.objects.filter(user = request.user).first()
        salary = account.salary()
    except:
        account = Accounts.objects.filter(user = request.user).first()
        salary = None
    param = {
        'email' : email,
        'username' : username,
        'account' : account ,
        'salary' : salary,
        'profile' : profile
    }
    
    return render(request , 'profile.html',param)
