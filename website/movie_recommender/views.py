from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import pickle
import numpy as np

# Create your views here.
def home(request):
	x=open('/home/shagun/Documents/movie_dataset','rb')
	data=pickle.load(x)
	return render(request,'home.html')	


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


def get_title_from_index(index):

	x=open('/home/shagun/Documents/movie_dataset','rb')
	data=pickle.load(x)
	return data[data.index==index]['title'].values[0]

def get_index_from_title(title):

	x=open('/home/shagun/Documents/movie_dataset','rb')
	data=pickle.load(x)
	return data[data.title==title]['index'].values[0]  	


def get_recommendations():

	f= open('/home/shagun/Documents/Ml Projects/Context_recommender_model','rb')
	context_model=pickle.load(f)	

	movie_index=get_index_from_title('Captain America: Civil War')
	similar_movies=list(enumerate(context_model[movie_index]))
	sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)	

	return sorted_similar_movies

def show_movies(request):
    movies_list=get_recommendations() 
    i=0
    dict={}
    list=[]
    for movie in movies_list:
        i+=1
        list.append(get_title_from_index(movie[0]))
        if i==50:
        	break

    return render(request,'recommendations.html',{'key':list})    	
       	


