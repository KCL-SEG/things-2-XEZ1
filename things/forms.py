from django import forms
from .models import User, Thing
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
        'description' : forms.Textarea(),
        'quantity' : forms.NumberInput()
        }

    name = forms.CharField(
        label='name',
        validators=[RegexValidator(
            message='Maximum length is 35.'
            )]
    )

    description = forms.CharField(
        label='description',
        validators=[RegexValidator(
            message='Description can be blank and up to 120 characters.'
            )]
    )

    quantity = forms.IntegerField(
        label='quantity',
        validators=[MinValueValidator(0),MaxValueValidator(50),
            RegexValidator(
            message='Number should be between 0 and 50.'
            )]
    )


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { 'bio' : forms.Textarea() }

    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message='Password must contain an uppercase character, a lowercase '
            'character and a number'
            )]
    )

    password_confirmation = forms.CharField(
    label='Password confirmation', widget=forms.PasswordInput()
    )

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')
