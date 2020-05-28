from django import forms

class MoviesForm(forms.Form):
	movie1=forms.CharField(max_length=40)
	rating1=forms.IntegerField(min_value=1,max_value=5,required=False)
	movie2=forms.CharField(max_length=40,required=False)
	rating2=forms.IntegerField(min_value=1,max_value=5,required=False)
	movie3=forms.CharField(max_length=40,required=False)
	rating3=forms.IntegerField(min_value=1,max_value=5,required=False)
	movie4=forms.CharField(max_length=40,required=False)
	rating4=forms.IntegerField(min_value=1,max_value=5,required=False)
	movie5=forms.CharField(max_length=40,required=False)
	rating5=forms.IntegerField(min_value=1,max_value=5,required=False)

	