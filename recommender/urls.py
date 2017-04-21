from django.conf.urls import url

from . import views
from . import restaurants

app_name = 'recommender'
urlpatterns = [
    url(r'^$', views.createPerson, name='createPerson'),
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^restaurants/$', restaurants.getRestaurants, name='getRestaurants'),
]
