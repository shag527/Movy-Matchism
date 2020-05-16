from django import form

class MoviesForm(forms.Form):
	movie1=forms.CharField(max_length=40)
	rating1=forms.IntegerField(min_value=1,max_value=5,null=True,blank=True)
	movie2=forms.CharField(max_length=40,max_value=5,null=True,blank=True)
	rating2=forms.IntegerField(min_value=1,max_value=5,max_value=5,null=True,blank=True)
	movie3=forms.CharField(max_length=40,max_value=5,null=True,blank=True)
	rating3=forms.IntegerField(min_value=1,max_value=5,max_value=5,null=True,blank=True)
	movie4=forms.CharField(max_length=40,max_value=5,null=True,blank=True)
	rating4=forms.IntegerField(min_value=1,max_value=5,max_value=5,null=True,blank=True)
	movie5=forms.CharField(max_length=40,max_value=5,null=True,blank=True)
	rating5=forms.IntegerField(min_value=1,max_value=5,max_value=5,null=True,blank=True)

	