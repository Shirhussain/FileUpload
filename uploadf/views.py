from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book
from django.urls import reverse_lazy
class FileHome(TemplateView):
	template_name = "home.html"

def upload(rquest):
	context = {}
	if rquest.method == "POST":
		upload_file = rquest.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(upload_file.name,upload_file)
		url = fs.url(name)
		context['url']= fs.url(name)
	return render(rquest,"upload.html", context)



def book_list(rquest):
	books = Book.objects.all()
	return render(rquest,"book_list.html",{'books':books})


def upload_book(rquest):
	if rquest.method == "POST":
		form = BookForm(rquest.POST, rquest.FILES)
		if form.is_valid():
			form.save()
			return redirect("books")
	else:
		form = BookForm()
	return render(rquest,"upload_book.html",{'form':form})


class BookListView(ListView):
	model = Book 
	template_name = "class_book_list.html"
	context_object_name = "books"


class UploadBookView(CreateView):
	model = Book
	template_name = "upload_book.html"
	form_class = BookForm
	# fields = ('title','author','pdf','cover')
	success_url = reverse_lazy("class_books")


def delete_book(rquest,pk):
	if rquest.method == 'POST':
		book = Book.objects.get(pk=pk)
		book.delete()
	return redirect("books")