from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	dict={'name':'Maze runner','rating':5}
	return render(request,'home.html',dict)