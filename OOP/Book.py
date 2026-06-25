class Book:
    def __init__ (self, author : str, title : str, price : int):
        self.author = author
        self.title = title
        self.price = price
    
    def display_info(self):
        print("Name of Book: ",self.title,", author: ",self.author,", price: ",self.price)


b = Book("Shantanu","Bita Din",399)
b.display_info()