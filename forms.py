from django import forms

class CommentForm(forms.Form):
    author=forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'class':'form_control',
        'placeholder':'your name',
    }))

    body=forms.CharField(max_length=60, widget=forms.Textarea(attrs={
        'class':'form_control',
        'placeholder':'your comment',
    }))