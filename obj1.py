from abc import ABC, abstractmethod
#IM SORRY FOR OUTDATING MY WORK

class Subscription(ABC):            
    def __init__(self,monthly_fee,min_period,channels,features):
        self.monthly_fee =monthly_fee
        self.min_period =min_period
        self.channels =channels
        self.features =features
 
    @abstractmethod
    def get_details(self):
        pass
#########################################################################

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=10,
                        min_period=6, 
                        channels=["News","Entertainment","Sports"],
                        features=["HD"])
    
    def get_details(self):
        return "Domestic Subscription: $10/month | MIN. PERIOD: 6 MONTHS"

class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=8, 
                        min_period=12, 
                        channels=["Science","History","Documentary"],
                        features=["HD","No Ads"])
    def get_details(self):
        return "Educational Subscription: 5$/month | MIN. PERIOD: 12 Month"

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=20,
                        min_period=3, 
                        channels=["All Channels Avaible"],
                        features=["4K", "No Ads", "Exclusive/Unique Content | MIN. PERIOD: 3 Month:"])
    
    def get_details(self):
        return "Premium Subscription: 20$/month"

    
#фабричний метод
class SubFactory(ABC):
    @abstractmethod
    def create_subscription(self, type):
        pass

#конкретні фабрики
class WebSite(SubFactory):
    def create_subscription(self,t):
        if t == "Domestic":
            return DomesticSubscription()
        elif t == "Educational":
            return EducationalSubscription()
        elif t == "Premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown Subscription Type")



class MobilkaApps(SubFactory):
    def create_subscription(self,type):
        return WebSite().create_subscription(type)
class ManCall(SubFactory):
    def create_subscription(self,type):
        return WebSite().create_subscription(type)
    
if __name__ == "__main__":
    website = WebSite()
    mobile_app = MobilkaApps()
    manager = ManCall()

    sub1 = website.create_subscription("Domestic")
    sub2 = mobile_app.create_subscription("Educational")
    sub3 = manager.create_subscription("Premium")

    print(sub1.get_details())
    print(sub2.get_details())
    print(sub3.get_details())

