from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import UserForm
from .models import User
from django.contrib import messages
# Create your views here.
def Registeruser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
        # create the user using the form for hashing the password
            # pass_hashing = form.cleaned_data['password']
            # u = form.save(commit=False)
            # u.set_password(pass_hashing)
            # u.role =User.CUSTOMER
            # u.save()
            # return redirect('Registeruser')

        # create the user using the create user method  for hashing the password
            first_hashing = form.cleaned_data['first_name']
            last_hashing = form.cleaned_data['last_name']
            username_hashing = form.cleaned_data['username']
            email_hashing = form.cleaned_data['email']
            password_hashing = form.cleaned_data['password']
            u = User.objects.create_user(first_name=first_hashing,last_name=last_hashing,
                                         username=username_hashing,email=email_hashing,
                                         password=password_hashing)
            u.role = User.CUSTOMER
            u.save()
            print("User created with hashing password successfully")
            messages.success(request,'Your account has been created succesfully!')
            return redirect('Registeruser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {

        'form':form
    }
        

    return render(request,'accounts/register.html',context)