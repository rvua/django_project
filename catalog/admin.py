from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

#admin.site.register(Book)
# Register the admin classes for Book using the decorator. This does
# the same thing as (admin.site.register() syntax.)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'word')
    list_filter = ['word'] 
    inlines = [BookInstanceInline]
    

class BookInline(admin.TabularInline):
    model = Book 
    extra = 0

#admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') 
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
# Note: Fields are displayed vertically by default, but will display horizontally if 
# you further group them in a tuple as shown in the "date" fields above.
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin) 

admin.site.register(Genre)

#admin.site.register(BookInstance)
# Register the admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = (id, 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            "fields": (
                'book',
                'imprint', 
                'id',
            ),
        }),
        ('Availability', {
            "fields": (
                'status',
                'due_back'
            )
        })
    )

    