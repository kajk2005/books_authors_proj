from django.urls import path
from. import views

urlpatterns = [
    path('add_book_to_author/<int:author_id>', views.add_book_to_author),
    path('author/<int:author_id>', views.author_info),
    path('add_author_to_books/<int:book_id>', views.add_author_to_book),
    path('books/<int:book_id>', views.single_book),
    path('add_authors', views.add_author),
    path('authors', views.authors),
    path('add_book', views.add_book),
    path('', views.index)

]
