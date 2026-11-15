from django.contrib import admin

from myapp.models import Book

# Register your models here.
admin.site.site_title = "Bookshop"
admin.site.site_header = "Bookshop Admin"
admin.site.index_title = "Bookshop Management System"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','isbn','category','cost')
    search_fields = ('title','isbn','category','year')
    list_filter = ('category','year')
    ordering = ('title', 'category','year')
