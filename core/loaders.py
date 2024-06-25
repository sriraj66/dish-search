import json
from core.models import *
import pandas as pd


class Loaders:
    
    def __init__(self):
        self.file = "data/restaurants_small.csv"
        self.data = pd.read_csv(self.file)
        
            
    def load_into_models(self,pid,name,location,lat_long,menu,full_details):
        res = Restaurant(
            pid=pid,name=name,location=location,lat_long=lat_long,
            menu=menu,full_details=full_details
        )
        res.save()
        res.get_res_details()
        items = res.get_menu_items()
        
        for i in items.keys():
            try:
                print(f"{i} : {items[i]}")
                if(type(items[i])==type("string")):
                    items[i] = items[i].split()[0]
                food = Items(
                    name = i,
                    price = float(items[i]),
                    res = res
                )
                food.save()
            except Exception as e:
                print(f"Error Loading Items: {e}")
        
    def load_restaurents(self):
        for i in range(len(self.data)):
            res = self.data.iloc[i]
            
            print(f"{res['name'] }- {res['location']}")
            self.load_into_models(res['id'],res['name'],res['location'],res['lat_long'],res['items'],res['full_details'])
            print("done..")
    

if __name__ == "__main__":
    load = Loaders()
    load.load_restaurents()