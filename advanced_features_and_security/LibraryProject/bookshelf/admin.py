from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to be used in displaying the User model.
    model = CustomUser
    
    # The fields to be displayed on the user's detail view page.
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # The fields to be displayed on the user creation page.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # List of fields to be displayed in the user list view.
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    
    # Fields that are searchable.
    search_fields = ('username', 'email')
    
    # Ordering of the user list view.
    ordering = ('username',)

# Register the CustomUser model with the CustomUserAdmin class.
admin.site.register(CustomUser, CustomUserAdmin)
