from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):

    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    name_short_url=forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "form-control form-control-lg", "placeholder": "Name (Optional)"}))

    duration_expire=forms.IntegerField(required=False, widget=forms.Textarea(
        attrs={"class": "form-control form-control-lg", "placeholder": "Duration (Optional): 7 days"}))

    class Meta:
        model = Shortener

        fields = ('long_url', 'name_short_url', 'duration_expire')

