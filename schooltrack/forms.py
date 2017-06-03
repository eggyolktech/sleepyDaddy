from django import forms

class SchoolForm(forms.Form):
    search_school = forms.CharField(label='Search School', max_length=100)