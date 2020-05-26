class Book:
    
    def __init__(self, id, title, author, pages, min_age):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.available = True
        self.min_age = min_age

    def __str__(self):
        return self.title + " by  " + self.author
    
    def get_book(self, id):
        pass

    def borrow(self):
        if self.available:
            self.available = False
        
        print('Book {0} borrowed'.format(self.title))

    def return_book(self):
        if not self.available:
            self.available = True
        
        print('Book {0} returned'.format(self.title))
