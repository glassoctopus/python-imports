from appliances import Appliance
class Stove(Appliance):

    def __init__(self, color, heat_method="electric"):
        super.__init__(color)

    def make_coffee(self): #should be a stove method
        print("gurgle, gurgle. Ding. Your drug of choice is piping hot and ready!")
