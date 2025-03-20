from abc import ABC, abstractmethod
#IM SORRY FOR OUTDATING MY WORK

class Laptop(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Netbook(ABC):
    @abstractmethod
    def get_details(self):
        pass

class EBook(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Smartphone(ABC):
    @abstractmethod
    def get_details(self):
        pass

class IProneLaptop(Laptop):
    def get_details(self):
        return "IProne Laptop: High-end device with exclusive OS" #chatgpt helped me with the description

class KiaomiLaptop(Laptop):
    def get_details(self):
        return "Kiaomi Laptop: Budget-friendly performance laptop" #chatgpt helped me with the description

class BalaxyLaptop(Laptop):
    def get_details(self):
        return "Balaxy Laptop: Durable and long-lasting business laptop" #chatgpt helped me with the description

class IProneSmartphone(Smartphone):
    def get_details(self):
        return "IProne Smartphone: Premium smartphone with unique features" #chatgpt helped me with the description

class KiaomiSmartphone(Smartphone):
    def get_details(self):
        return "Kiaomi Smartphone: Affordable smartphone with solid specs" #chatgpt helped me with the description

class BalaxySmartphone(Smartphone):
    def get_details(self):
        return "Balaxy Smartphone: Powerful smartphone with advanced display" #chatgpt helped me with the description

######################################################################################################################

class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass
    
    @abstractmethod
    def create_smartphone(self):
        pass

class IProneFactory(DeviceFactory):
    def create_laptop(self):
        return IProneLaptop()
    
    def create_smartphone(self):
        return IProneSmartphone()

class KiaomiFactory(DeviceFactory):
    def create_laptop(self):
        return KiaomiLaptop()
    
    def create_smartphone(self):
        return KiaomiSmartphone()

class BalaxyFactory(DeviceFactory):
    def create_laptop(self):
        return BalaxyLaptop()
    
    def create_smartphone(self):
        return BalaxySmartphone()

if __name__ == "__main__":
    ipf = IProneFactory()
    kiaomifactory = KiaomiFactory()
    balaxyfactory = BalaxyFactory()
    iproneLaptop = ipf.create_laptop()
    kiaomismartphone = kiaomifactory.create_smartphone()
    balaxylaptop = balaxyfactory.create_laptop()
    
    print(iproneLaptop.get_details())
    print(kiaomismartphone.get_details())
    print(balaxylaptop.get_details())

