from django import forms
from users.models import user



class signup_form(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

    # name = forms.CharField()
    # age = forms.IntegerField()
    # email = forms.EmailField()