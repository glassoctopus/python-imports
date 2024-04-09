from appliances import DishWasher
from appliances import Dryer
from appliances import Washer
from appliances import Refrigerator
from appliances import CoffeeMaker

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "super_scrub")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()
