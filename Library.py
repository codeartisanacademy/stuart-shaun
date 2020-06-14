class Library:
    
    # constructor
    def __init__(self, id, name, city, books, members):
        self.id = id
        self.name = name
        self.city = city
        self.books = books
        self.members = members
        self.borrowers = []


    def __str__(self):
        return self.name + " in " + self.city

    def borrowed_books(self):
        # print and return all the books and the person who borrow
        # Python Book borrowed  by Budi
        for book in self.borrowers:
            print(book['member'].full_name + ' borrows ' + book['book'].title)

    def available_books(self):
        avaiable_books = []
        for b in self.books:
            if b.available:
                avaiable_books.append(b)
                print(b)
        
        return avaiable_books
    

    def list_all_books(self):
        for b in self.books:
            print(b)

    def retrieve_book(self, book):
        for b in self.borrowers:
            if b['book'] == book:
                self.borrowers.remove(b)