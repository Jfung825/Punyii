class Book:
    Book_count = 0
    def __init__(self ,title,author,page):
        self.title = title
        self.author = author
        self.page = page
        Book.Book_count += 1
    
    def summary(self):
        print(self.title,"by",self.author,self.page,"pages")
        

b1 = Book("The Hoblord","SteveG",255)    
b2 = Book("The Robbit","Layen mayal",10)  

print("-"*20)
b1.summary()
b2.summary()
print("-"*20)