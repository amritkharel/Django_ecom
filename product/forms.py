# products/forms.py
from django import forms

class ReviewForm(forms.Form):
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea)
