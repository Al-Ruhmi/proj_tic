from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import User
from .form import RegisterStudentForm,UpdateStudentForm
from .decorators import unauthentticated_user
# Create your views here.


# تسجيل حساب الطالب
@unauthentticated_user
def register_student(request):
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_student = True
            var.save()
            messages.info(request, 'Your account has been registered .. Please Login to continou !')
            return redirect('login')
        else:
            messages.warning(request , 'Sorry Something Went Worng . Please Check The Entered Values')
            return redirect('register_student')
    else:
        form = RegisterStudentForm()
        context = {'form':form}
        return render(request, 'users/register_student.html', context)
    
# تسجيل الدخول 
@unauthentticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request, 'Logged Successfull .. !')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something Went Worng Please Check UserName And Passowrd .. !')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
# تسجيل الخروج 
def logout_user(request):
    logout(request)
    messages.info(request, 'You Are Logging out .. !')
    return redirect('login')





def student_details(request):
    std = User.objects.all()
    context = {'std':std}
    return render(request, 'users/student_details.html', context)

@login_required
def update_student(request, pk):
    # std = StdUser.objects.get(user=request.user)
    # user = request.user
    user = User.objects.get(pk=pk)
    form = UpdateStudentForm(instance=user)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST,request.FILES, instance=user)
        # if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request, 'users/update_student.html', context)

