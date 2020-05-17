from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from uploadf.views import FileHome, upload, book_list, upload_book,BookListView,UploadBookView,delete_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',FileHome.as_view(), name="home"),
    path('delete_book/<int:pk>/',delete_book, name="delete_book"),
    # path('upload/', upload, name="upload"),
    path('books/',book_list, name="books"),
    path("books/upload",upload_book, name="upload"),
    path("class/books/",BookListView.as_view(), name="class_books"),
    path("class/book/uplaod/",UploadBookView.as_view(), name="class_upload")
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)