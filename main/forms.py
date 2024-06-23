from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            "name": "msg",
            "id": "msg",
            "cols": 30,
            "rows": 5,
            "class": "form-control",
            "style": "background-color: black;"
        })
