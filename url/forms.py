from django import forms
from .models import Url
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from .utils import create_shortcode

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUrlForm(forms.ModelForm):
    """Form definition for CreateUrl."""
    class Meta:
        """Meta definition for CreateUrlform."""

        model = Url
        fields = ('actual_url','shortcode')

    def clean_actual_url(self):
        # print('I am validating URL')
        url_v = self.cleaned_data['actual_url']
        # print('url_v: ' + str(url_v))
        try:
            validate = URLValidator(
                    schemes=("http", "https", "ftp", "ftps", "rtsp", "rtmp")
                )
            validate(url_v)
        except:
            # print('Invalid URL')
            raise ValidationError('Enter correct URL')
        return url_v
        
    def clean_shortcode(self):
        # print('I am here to validate shortcode')
        sc = self.cleaned_data['shortcode']
        if sc == None:
            sc = create_shortcode()
        if len(sc)<5 or len(sc)>15:
            raise ValidationError('Minimum and Maximum shortcode length can be 5 and 15 respectively')
        if Url.objects.filter(shortcode=sc).exists():
            raise ValidationError('Cannot process this code, enter another unique code')
        return sc

class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username','password1','password2']