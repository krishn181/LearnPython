from abc import ABC, abstractmethod
class Password:
    @abstractmethod
    def password(self):
        pass
        
class UpiPassword(Password):
    def __init__(self, password:str):
        self.password = password
    
    def upi_password(self):
        return self.password

upi = UpiPassword(1234)
print(upi.upi_password())