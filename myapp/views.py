from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import Book
from myapp.my_form import BookForm


# Create your views here.
def show_books(request):
    books = Book.objects.all()
    return render(request, 'show_books.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book {request.POST.get('title')} Created')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def delete_book(request, id):
    book = Book.objects.get(id=id) #select * from books where id = 34
    book.delete() #delete from books where id = 34
    messages.error(request, f'{book.title} Deleted Successfully')
    return redirect('show_books')


def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title} Updated Successfully')
            return redirect('show_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})



# Book.objects.create(title='A Silent Song',
#                     year=2024,
#                     category = 'Fiction',
#                     cost = 500,
#                     isbn='234567898765',
#                     published = True)
# Book.objects.create(title='Blossoms of the Savanna',
#                     year=2009,
#                     category='Fiction',
#                     cost = 499,
#                     isbn='5678987655',
#                     published=True)
