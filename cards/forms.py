from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.ImageField(required=True)
    solved = forms.BooleanField(required=True)