from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic	# To create class based view function
# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_books=Book.objects.all().count()
	num_instances=BookInstance.objects.all().count()
	#Available books(status='a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count()	# The 'all()' is implied by default

	# Render the HTML template index.html with the data in the text variable
	return render(
		request,
		'index.html',
		context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
		)

class BookListView(generic.ListView):
	model = Book
	context_object_name = 'my_book_list'
	queryset = Book.objects.filter(title_icontains='programming')[:5] # Get 5 Books containg the title 'programming'
	template_name = 'books/my_arbitrary_templatete_name_list.html'

	def get_queryset(self):
		return Book.objects.filter(title_icontains='programming')[:5] # Get 5 books with title 'programming'
	
	def get_context_data(self, **kwargs):
		context = super(BookListView,self).get_context_data(**kwargs)
		context['some_data'] = 'This is just some data'
		return context		