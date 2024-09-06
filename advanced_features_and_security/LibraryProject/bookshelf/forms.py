# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book  # Import your model here

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model this form is associated with
        fields = ['title', 'author', 'published_date']  # Specify the fields to include in the form
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})  # Customize widgets if needed
        }

    # Optionally, add custom validation methods here
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'badword' in title:
            raise forms.ValidationError("Invalid word in title.")
        return title