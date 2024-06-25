from django.db import models
import json

class Restaurant(models.Model):
    pid = models.PositiveIntegerField()
    name = models.CharField(max_length=255,verbose_name="Name")
    location = models.CharField(max_length=255,verbose_name="Location")
    lat_long = models.CharField(max_length=255,verbose_name="Lat-Long",default="")
    menu = models.TextField(verbose_name="Items")
    full_details = models.TextField()
    city = models.CharField(max_length=255,verbose_name='City',blank=True)
    
    # EVALUTION
    user_rating = models.CharField(max_length=255,verbose_name='User rating',default="None")
    votes = models.IntegerField(default=0)
    avg_rating = models.FloatField(default=0)
    
    created = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name.capitalize()
    
    def get_menu_items(self):
        try:
            data = json.loads(self.menu)
            return data
        except Exception as e:
            print("Error: ", e)
        return {}
    
    def get_res_details(self):
        try:
            try:
                data = json.loads(self.full_details)
            except Exception as e:
                print("Error: Unable to Load.. ", e)
                return {}
            self.city = data['location']['city']
            self.user_rating = data['user_rating']["rating_text"]
            self.avg_rating = float(data['user_rating']['aggregate_rating'])
            self.votes = int(data['user_rating']['votes'])
            self.save()
            return data
        except Exception as e:
            print("Error: ", e)
        return {}

class Items(models.Model):
    name = models.CharField(max_length=255,verbose_name="Item Name")
    price = models.FloatField()
    res = models.ForeignKey(Restaurant, blank=True,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name.capitalize()
    