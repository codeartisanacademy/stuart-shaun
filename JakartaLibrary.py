#  from File import everything
from Book import *
from Member import *
from Library import *

# prepare and add the books 
books = []
python_book = Book(id=1, title = 'Python Book', author='John', pages=100, min_age=12)
java_book = Book(id=2, title = 'Java Book', author='Jim', pages=200, min_age=12)
doraemon_book = Book(id=3, title='Doraemon and Friends', author='Shaun & Stuart', pages=20, min_age=3)
books.append(python_book)
books.append(java_book)
books.append(doraemon_book)

members = []
budi = Member(1, 'Budi Wijaya', 'budi@gmail.com', '1999-10-2')
john = Member(full_name='John Doe', id=2, email='john@gmail.com', birthday='2016-11-12')
members.append(budi)
members.append(john)

jakarta_library = Library(id=1, name='Jakarta Library', city='Jakarta', books=books, members=members)

print(jakarta_library.available_books())

# budi borrows python book
python_book.borrow()
borrower = {'member': budi, 'book':python_book}
jakarta_library.borrowers.append(borrower)

doraemon_book.borrow()
borrower_doraemon = {'member': john, 'book':doraemon_book}
jakarta_library.borrowers.append(borrower_doraemon)

jakarta_library.available_books()

jakarta_library.borrowed_books()