from rest_framework import serializers
from .models import Movies_list

class Movies_list_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Movies_list
		fields='__all__'