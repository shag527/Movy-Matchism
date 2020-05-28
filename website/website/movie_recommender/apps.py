from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class MovieRecommenderConfig(AppConfig):
    name = 'movie_recommender'

    #creating path to models

    context_path=os.path.join(settings.MODELS,'Context_recommender_model')
    collaborative_path=os.path.join(settings.MODELS,'Collaborative_recommender_model')
    data_path=os.path.join(settings.MODELS,'movie_dataset')

    #load models into seperate variables

    f1= open(context_path,'rb')
    context_model=pickle.load(f1)

    f2=open(collaborative_path,'rb')
    Collaborative_model=pickle.load(f2)	

    x=open(data_path,'rb')
    data=pickle.load(x)	

