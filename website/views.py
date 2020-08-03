from django.shortcuts import render,redirect
# from datetime import datetime
from website.models import Contact
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

from django.contrib import messages

# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request,'register.html',context)
   
   

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request,'login.html',context)
        
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def room(request):
    return render(request,'rooms.html')

@login_required(login_url='login')
def service(request):
    return render(request,'services.html')

@login_required(login_url='login')
def contact(request):
	if request.method == "POST":
		message = request.POST.get('message')
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		contact = Contact(message=message, name=name, email=email, subject=subject)
		contact.save()
		messages.success(request, "Your message has been sent to the Mister D's Hotel admin staff.")
	return render(request,'contact.html')