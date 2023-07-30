from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signin(request):
    if request.method == "GET":
        return render(request, 'signin/signin.html')
    else:
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')
        
        isAuth = authenticate(username=user, password=passwd)

        if isAuth is not None:
            login(request, isAuth)
            return redirect('home')
            
        else:
            messages.error(request, "Nome de usuario ou senha invalidos")
            return redirect('signin')

@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, 'signup/signup.html')

    else:
        name = request.POST.get('name')
        username = request.POST.get('user')
        passwd = request.POST.get('passwd')

        hasUser = User.objects.filter(username=username).first()
        
        if len(passwd) < 5:
            messages.error(request, "A senha deve possuir no minimo 5 carateres")
            return redirect('signup')

        if hasUser:
            messages.error(request, "Já existe um usuario com esse nome")
            return redirect('signup')
        

        new_user = User.objects.create_user(username=username, password=passwd, first_name=name)
        new_user.save()

        messages.success(request, "Cadastro finalizado, você ja pode realizar login")
        return redirect('signup')

@csrf_exempt
@login_required(login_url='signin')
def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            task = request.POST.get('task')
            newTask = Task(user=request.user, task=task)
            hasTask = Task.objects.filter(task=task).first()
            if hasTask:
                messages.error(request, "As taferas devem ter nomes diferentes")
            else:
                newTask.save()
        allTasks = Task.objects.filter(user=request.user)
        name = User.objects.filter(username=request.user)
        context = {
            'tasks': allTasks,
            'name': name
        }
        return render(request, 'home/home.html', context)      
    else:
        return render(request, 'signin/signin.html')    


@login_required
def log_out(request):
    logout(request)
    return redirect('signin')

@csrf_exempt
def deletTask(request, name):
    getTask = Task.objects.filter(user=request.user, task=name)
    getTask.delete()
    return redirect('home')

@csrf_exempt
def completTask(request, name):
    getTask = Task.objects.filter(user=request.user, task=name)
    for task in getTask:
        task.status = True
        task.save()
    return redirect('home')