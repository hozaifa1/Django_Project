from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', )

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'type': 'text', 'placeholder': 'Search', 'aria-label': 'Search'}))