
from django import forms
from django.forms import ModelForm
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm,SetPasswordForm

from django.contrib.auth import (get_user_model,)
import os
import re

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Customer,Cleaner



TRANSPOSE_CHOICES = (
    ("", u"-----"),
    ("0", _(u"Flip horizontal")),
    ("1", _(u"Flip vertical")),
    ("2", _(u"Rotate 90° CW")),
    ("4", _(u"Rotate 90° CCW")),
    ("3", _(u"Rotate 180°")),
)


class CreateDirForm(forms.Form):
    """
    Form for creating a folder.
    """

    name = forms.CharField(widget=forms.TextInput(attrs=dict({'class': 'vTextField'}, max_length=50, min_length=3)), label=_(u'Name'), help_text=_(u'Only letters, numbers, underscores, spaces and hyphens are allowed.'), required=True)

    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.site = kwargs.pop("filebrowser_site", None)
        super(CreateDirForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        "validate name"
        if self.cleaned_data['name']:
            # only letters, numbers, underscores, spaces and hyphens are allowed.
            if not ALNUM_NAME_RE.search(self.cleaned_data['name']):
                raise forms.ValidationError(_(u'Only letters, numbers, underscores, spaces and hyphens are allowed.'))
            # Folder must not already exist.
            if self.site.storage.isdir(os.path.join(self.path, convert_filename(self.cleaned_data['name']))):
                raise forms.ValidationError(_(u'The Folder already exists.'))
        return convert_filename(self.cleaned_data['name'])


class ChangeForm(forms.Form):
    """
    Form for renaming a file/folder.
    """

    custom_action = forms.ChoiceField(label=_(u'Actions'), required=False)
    name = forms.CharField(widget=forms.TextInput(attrs=dict({'class': 'vTextField'}, max_length=50, min_length=3)), label=_(u'Name'), help_text=_(u'Only letters, numbers, underscores, spaces and hyphens are allowed.'), required=True)

    def __init__(self, *args, **kwargs):
        self.path = kwargs.pop("path", None)
        self.fileobject = kwargs.pop("fileobject", None)
        self.site = kwargs.pop("filebrowser_site", None)
        super(ChangeForm, self).__init__(*args, **kwargs)

        # Initialize choices of custom action
        choices = [("", u"-----")]
        for name, action in self.site.applicable_actions(self.fileobject):
            choices.append((name, action.short_description))
        self.fields['custom_action'].choices = choices

    def clean_name(self):
        "validate name"
        if self.cleaned_data['name']:
            # only letters, numbers, underscores, spaces and hyphens are allowed.
            if not ALNUM_NAME_RE.search(self.cleaned_data['name']):
                raise forms.ValidationError(_(u'Only letters, numbers, underscores, spaces and hyphens are allowed.'))
            #  folder/file must not already exist.
            if self.site.storage.isdir(os.path.join(self.path, convert_filename(self.cleaned_data['name']))) and os.path.join(self.path, convert_filename(self.cleaned_data['name'])) != self.fileobject.path:
                raise forms.ValidationError(_(u'The Folder already exists.'))
            elif self.site.storage.isfile(os.path.join(self.path, convert_filename(self.cleaned_data['name']))) and os.path.join(self.path, convert_filename(self.cleaned_data['name'])) != self.fileobject.path:
                raise forms.ValidationError(_(u'The File already exists.'))
        return convert_filename(self.cleaned_data['name'])
        

User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="User name", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'username' }))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'password'}))


class Password_reset(PasswordResetForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Enter Your Email'}))
 
    

class Set_Password(SetPasswordForm):
    password= forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1'}))
    password2= forms.CharField(label="Conform Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2'}))

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'required': True, 'placeholder': 'Enter Username', 'size': 38}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'required': True, 'placeholder': 'Password', 'size': 38}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={ 'required': True, 'placeholder': 'confirm password', 'size': 38}))
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            # 'password2',
        ]
    def clean(self):
      cleaned_data = super(UserRegisterForm, self).clean()
      password = self.cleaned_data.get('password')
      confirm_password = self.cleaned_data.get('confirm_password')
      if password and password != confirm_password:
        raise forms.ValidationError("password and confirm_password does not match")

# CITY_CHOICES = (
#     ('Pune', 'Pune'),
#     ('Mumbai', 'Mumbai'),
#     ('Vadodara', 'Vadodara'),
#     ('Jabalpur', 'Jabalpur'),
#     ('Bhopal', 'Bhopal'),
#     ('Trivandrum', 'Trivandrum'),
#     ('Chennai', 'Chennai'),
#     ('Kochi', 'Kochi'),
#     ('Kolkata', 'Kolkata'),
    
#     ('Indore', 'Indore'),

#     )
MODEL_CATEGORIES = (
        ('Pune', 'Pune'),
        ('Mumbai', 'Mumbai'),
        ('Vadodara', 'Vadodara'),
        ('Jabalpur', 'Jabalpur'),
        ('Bhopal', 'Bhopal'),
        ('Trivandrum', 'Trivandrum'),
        ('Chennai', 'Chennai'),
        ('Kochi', 'Kochi'),
        ('Kolkata', 'Kolkata'),
        ('Indore', 'Indore'),
        
    )

class Customer_form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    # city = forms.MultipleChoiceField(choices=CITY_CHOICES,widget=forms.CheckboxSelectMultiple(attrs={'required': True}))
    # city = forms.MultipleChoiceField(
    # required=True,
    # choices=CITY_CHOICES
    # )
    # phone_number = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    
    # city = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=FAVORITE_COLORS_CHOICES,
    # )
    city = forms.MultipleChoiceField(
            widget = forms.CheckboxSelectMultiple,
            choices = MODEL_CATEGORIES
    )
    
    class Meta:
        model = Customer
        fields = ["first_name","last_name","phone_number","city"]



class Cleaner_form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    
    class Meta:
        model = Cleaner
        fields = ["first_name","last_name"]

