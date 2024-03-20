# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# # Single Responsibility Principle
# class Book:
#     def set_details(self, title, author):
#         pass
#     def get_discount_price(self, discount):
#         pass

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    
    def set_details(self, title, author):
        self.title = title
        self.author = author


    def get_discount_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return discounted_price
    

# ============================
    
book = Book("The Picture of Dorian Gray", "Oscar Wilde", 50)
print("Original Price:", book.price)
print("Discounted Price (10% off):", book.get_discount_price(10))