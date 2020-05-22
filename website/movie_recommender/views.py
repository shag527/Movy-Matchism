from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Movies_list
import pickle
from . serializers import Movies_list_Serializer
from .forms import MoviesForm
import pandas as pd
from .apps import MovieRecommenderConfig

# Create your views here.


def profile(request):
	form=MoviesForm()
	return render(request,'profile.html',{'form':form})	


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


def get_title_from_index(index,data):
	try:
		return data[data.index==index]['title'].values[0]
	except:
		return HttpResponse('Provide Valid NAME')

def get_index_from_title(title,data):
	try:
		return data[data.title==title]['index'].values[0]  
	except:
		return HttpResponse('Provide Valid NAME')	

def get_score(movie,rating,model):
	score=model[movie]*(rating-2.5)
	score=score.sort_values(ascending=False)
	return score		


def get_context_recommendations(movie,data):
	try:
		context_model=MovieRecommenderConfig.context_model
		movie_index=get_index_from_title(movie,data)
		similar_movies=list(enumerate(context_model[movie_index]))
		sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)	
		return sorted_similar_movies

	except:
		return HttpResponse('Provide Valid NAME')

def get_collaborative_recommendations(movie,rating,list):
	try:
		Collaborative_model=MovieRecommenderConfig.Collaborative_model	
		list=list.append(get_score(movie,rating,Collaborative_model),ignore_index=True)
		return list
	except:
	    return HttpResponse('Not Valid')	


def show_context_movies(movie,list):
	try:
		data=MovieRecommenderConfig.data
		movies_list=get_context_recommendations(movie,data) 
		i=0
		for movie in movies_list:
			i+=1
			list.append(get_title_from_index(movie[0],data))
			if i==50:
				break   

	except:
		return HttpResponse('Provide Valid NAME')		


def show_collaborative_movies(list,Collaborative_list):	
        try:				
        	Collaborative_list=Collaborative_list.columns
        	i=0
        	for movie in Collaborative_list:
        		list.append(Collaborative_list[i])
        		i+=1
        		if i==50:
        			break
        	return list		

        except:
            return HttpResponse('Not valid')		


def check_seen(context_list,collaborative_final_list):
    final_list=[]
    for movie in context_list:
    	if movie not in final_list:
    		final_list.append(movie)

    for movie in collaborative_final_list:
    	if movie not in final_list:
    		final_list.append(movie)

    return final_list		



def home(request):
	if request.method=='POST':
		form=MoviesForm(request.POST)
		if form.is_valid():
			movie1=form.cleaned_data['movie1']
			rating1=form.cleaned_data['rating1']
			movie2=form.cleaned_data['movie2']
			rating2=form.cleaned_data['rating2']
			movie3=form.cleaned_data['movie3']
			rating3=form.cleaned_data['rating3']
			movie4=form.cleaned_data['movie4']
			rating4=form.cleaned_data['rating4']
			movie5=form.cleaned_data['movie5']
			rating5=form.cleaned_data['rating5']

		#print(final_list)
		
		#return render(request,'recommendations.html',{'key':(final_list)}) 


			
	form=MoviesForm()
	return render(request,'home.html',{'form':form})



class recommend_movies(APIView):

	def get(self, request):
		movies=Movies_list.objects.all()
		serializer=Movies_list_Serializer(movies,many=True)
		return Response({"movies":serializer.data})

	def post(self,request):
		data=request.data
		serializer=Movies_list_Serializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=201)
		return Response(serializer.erros,status=400)


class call_model(APIView):
	def get(self,request):
		if request.method=='GET':
			movie1=request.GET.get('movie1')
			rating1=request.GET.get('rating1')
			movie2=request.GET.get('movie2')
			rating2=request.GET.get('rating2')
			movie3=request.GET.get('movie3')
			rating3=request.GET.get('rating3')
			movie4=request.GET.get('movie4')
			rating4=request.GET.get('rating4')
			movie5=request.GET.get('movie5')
			rating5=request.GET.get('rating5')


			context_list=[]
			Collaborative_list=pd.DataFrame()	
			#print(movie1,movie2,movie3,movie4,movie5)
			if rating1:
				Collaborative_list=get_collaborative_recommendations(movie1,rating1,Collaborative_list)
				show_context_movies(movie1,context_list)
			else:	
				show_context_movies(movie1,context_list)
			if movie2:	
				if rating2:
					Collaborative_list=get_collaborative_recommendations(movie2,rating2,Collaborative_list)
					show_context_movies(movie2,context_list)
				else:	
					show_context_movies(movie2,context_list)
			if movie3:	
				if rating3:
					Collaborative_list=get_collaborative_recommendations(movie3,rating3,Collaborative_list)
					show_context_movies(movie3,context_list)
				else:	
					show_context_movies(movie3,context_list)
			if movie4:	
				if rating4:
					Collaborative_list=get_collaborative_recommendations(movie4,rating4,Collaborative_list)
					show_context_movies(movie4,context_list)
				else:	
					show_context_movies(movie4,context_list)
			if movie5:	
				if rating5:
					Collaborative_list=get_collaborative_recommendations(movie5,rating5,Collaborative_list)
					show_context_movies(movie5,context_list)
				else:	
					show_context_movies(movie5,context_list)

			collaborative_final_list=[]
			collaborative_final_list=show_collaborative_movies(collaborative_final_list,Collaborative_list)

			final_list=[]
			final_list=check_seen(context_list,collaborative_final_list)
			return JsonResponse({'key':final_list})