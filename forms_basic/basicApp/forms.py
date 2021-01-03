from django import forms
from django.core import validators

#custom validators
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.TextInput)

    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])


    # using your own botcatcher function
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError('Gotcha bot!!!')
    #     return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("emails need to match!!!")