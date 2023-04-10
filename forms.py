from django import forms

from .models import Booklog




class Booklogform(forms.ModelForm):
    class Meta:
        model = Booklog
        fields = "__all__"

