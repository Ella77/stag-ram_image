from __future__ import unicode_literals
from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):
    #rlwns
    class Meta:
        model =Photo
        fields= ('image','content',)