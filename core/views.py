from django.shortcuts import render
from .models import *
import math,random
from django.db.models import Count

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371 
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


def sort_search_results(search, user_lat, user_long):
    user_rating_mapping = {
        "Excellent": 5,
        "Very Good": 4,
        "Good": 3,
        "Average": 2,
        "Poor": 1,
        "None": 0
    }

    for result in search:
        lat, lon = map(float, result['lat_long'].split(","))
        result['distance'] = round(calculate_distance(user_lat, user_long, lat, lon),2)
        result['numeric_user_rating'] = user_rating_mapping.get(result['user_rating'], 0)

    search.sort(key=lambda x: (
        -x['rating'],  # Highest rating first
        x['distance'],  # Nearest location first
        -x['numeric_user_rating'],  # Highest user ratings first
        -x['votes'],  # Highest votes first
        x['price']  # Lowest price first
    ))



def index(request):
    context = {
        'results':[]
    }
    
    if request.method == 'POST':
        # from .loaders import Loaders
        # load = Loaders()
        # load.load_restaurents()
        pass
        
    return render(request,'core/index.html',context)



def search_results(request):
    
    context = {
        'results':[],
        
    }
    
    if request.method == 'POST':
        dish = request.POST.get('dish', "")
        location = request.POST.get("location","12.9118141,77.59711879999999")
        if len(location)<1:
            location = "12.9118141,77.59711879999999"
            
        lat,long = map(float,location.split(","))
        print(dish,location)
        if (len(dish)>=2):
            res = Items.objects.filter(name__icontains=dish.lower())
        else:
            res = []
        search = []
        notexist = False
        if len(res)<=0:
            res = Items.objects.annotate(num_items=Count('id')).order_by('?')[:6]
            notexist = True
            
        for i in res:
            results = {}
            results["name"] = i.name
            results['price'] = i.price
            results['res'] = i.res.name
            results['loc'] = i.res.location
            results['lat_long'] = i.res.lat_long
            results['rating'] = i.res.avg_rating
            results['user_rating'] = i.res.user_rating
            results['votes'] = i.res.votes
            search.append(results)

        if(len(search)>0):
            sort_search_results(search,lat,long)
        
        if notexist:
            context['alt'] = search
        else:
            context['results'] = search
        context['len'] = len(search)
        context['outof'] = len(Restaurant.objects.all())
            
    return render(request,"core/partial/results.html",context)
