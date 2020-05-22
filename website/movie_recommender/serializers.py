from rest_framework import serializers
from .models import Movies_list

<<<<<<< HEAD
class Movies_list_Serializer(serializers.ModelSerializer):
=======
class Movies_list_Serializer(serializers.HyperlinkedModelSerializer):
>>>>>>> c05054faa36ef02768daae5440025a5e9b0a1169
	class Meta:
		model=Movies_list
		fields='__all__'