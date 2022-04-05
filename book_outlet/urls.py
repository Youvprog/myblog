from django.urls import path
from . import views


urlpatterns = [
    path("", views.book_list),
    path("<slug:slug>", views.book_details, name="book_detail")
]
