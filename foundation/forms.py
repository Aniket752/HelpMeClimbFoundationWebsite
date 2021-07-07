from django import forms
from .models import donation,volunteer,massage,donationMade,recipt

class donate(forms.ModelForm):
    class Meta:
        model=donation
        fields="__all__"
class donateMade(forms.ModelForm):
    class Meta:
        model=donationMade
        fields="__all__"
class work(forms.ModelForm):
    class Meta:
        model=volunteer
        fields="__all__"
class massage(forms.ModelForm):
    class Meta:
        model=massage
        fields="__all__"
class reciptno(forms.ModelForm):
    class Meta:
        model=recipt
        fields="__all__"
