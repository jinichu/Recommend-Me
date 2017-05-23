from django.shortcuts import render
from urllib import quote
from urllib import urlencode
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from .models import Restaurant, Person, FoodType
import json
import requests

HOST = 'https://api.yelp.com'
TOKEN_PATH = '/oauth2/token'
SEARCH_PATH = '/v3/businesses/search'
SEARCH_LIMIT = 10
GRANT_TYPE = 'client_credentials'
CLIENT_ID = 'bKohbmTp65cNKrBI-xrt0A'
CLIENT_SECRET = 'jDTaXpUA2y6uwnFl1YmSas49j1XRAzQjyHruplt4kLjf9q7RunlMeuUwgRug2xfJ'

def getRestaurants(request):
    if request.method == 'POST':
        person = Person.objects.get(id=request.POST['person_id'])
        food_type_obj = FoodType.objects.get_or_create(type=int(request.POST['food_type']))[0]
        person.food_type = food_type_obj
        person.save()
        print person.food_type.get_type_display()
        bearer_token = obtain_bearer_token(HOST, TOKEN_PATH)
        response = search(bearer_token, food_type_obj.get_type_display(), request.POST['lat'], request.POST['lon'])
        businesses = response.get('businesses')
        restaurants = []
        print businesses[0]
        for business in businesses:
            r = Restaurant(name=business['name'], rating=business['rating'], address=business['location']['display_address'][0],
                phone=business['display_phone'], latitude=business['coordinates']['latitude'], longitude=business['coordinates']['longitude'])
            restaurants.append(r)
        content = {
            'restaurants': restaurants,
            'latitude': request.POST['lat'],
            'longitude': request.POST['lon']
        }
        return render(request, 'recommender/restaurants.html', content)
    else:
        return render(request, 'recommender/restaurants.html', {})

# Yelp API
def search(bearer_token, term, lat, lon):
    url_params = {
        'term': term.replace(' ', '+'),
        'latitude': lat,
        'longitude': lon,
        'limit': SEARCH_LIMIT,
        'sort_by': 'distance'
    }
    url = '{0}{1}'.format(HOST, quote(SEARCH_PATH.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }
    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()

def obtain_bearer_token(host, path):
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))

    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token
