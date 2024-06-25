from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
]

urlpatterns += [
    path("hx/search",views.search_results,name='search_results')
]