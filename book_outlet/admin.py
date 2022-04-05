from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.contrib import admin
from .models import Address, Book, Author, Country
# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author",)
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
