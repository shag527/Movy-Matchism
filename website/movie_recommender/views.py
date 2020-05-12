from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

# Create your views here.
def home(request):
	dict={'name':'Maze runner','rating':5}
	return render(request,'home.html',dict)	


def profile(request):
    return render(request,'profile.html')	    


def register(request):
	if request.method == 'POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=raw_password)
			login(request,user)
			return render(request,'profile.html')
		else:
			return HttpResponse('Invalid Form')
	else:
	    form=UserCreationForm()
	    args={'form':form}
	return render(request,'register.html',args)		
