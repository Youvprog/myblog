from audioop import reverse
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}, {self.code}"


# ------------------------------------------------------------------------------------
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}"
# -----------------------------------------------------------------------------------


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ------------------------------------------------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books")
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_book_details_path(self):
        return reverse("book_detail", args=[self.slug])
